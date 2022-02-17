# -*- coding: utf-8 -*-
# isort: skip_file
# fmt: off

"""This module contains the logic of resource management"""

import inspect
import re
from six import with_metaclass

from werkzeug.wrappers import Response
from flask import request, url_for, make_response
from flask.wrappers import Response as FlaskResponse
from flask.views import MethodView, MethodViewType
from marshmallow_jsonapi.exceptions import IncorrectTypeError
from marshmallow import ValidationError

from .querystring import QueryStringManager as QSManager
from .pagination import add_pagination_links
from .exceptions import InvalidType, BadRequest, RelationNotFound
from .decorators import check_headers, check_method_requirements
from .schema import compute_schema, get_relationships, get_model_field
from .data_layers.base import BaseDataLayer
from .data_layers.alchemy import SqlalchemyDataLayer
from .utils import json_dumps
from marshmallow_jsonapi.fields import BaseRelationship
from werkzeug.datastructures import ImmutableMultiDict


class ResourceMeta(MethodViewType):
    """Meta class to initilize the data layer and decorators of a resource"""

    def __new__(cls, name, bases, d):
        """Constructor of a resource class"""
        rv = super(ResourceMeta, cls).__new__(cls, name, bases, d)
        if 'data_layer' in d:
            if not isinstance(d['data_layer'], dict):
                raise Exception("You must provide a data layer information as dict in {}".format(cls.__name__))

            if d['data_layer'].get('class') is not None\
                    and BaseDataLayer not in inspect.getmro(d['data_layer']['class']):
                raise Exception("You must provide a data layer class inherited from BaseDataLayer in {}"
                                .format(cls.__name__))

            data_layer_cls = d['data_layer'].get('class', SqlalchemyDataLayer)
            data_layer_kwargs = d['data_layer']
            rv._data_layer = data_layer_cls(data_layer_kwargs)

        rv.decorators = (check_headers,)

        for b in bases or []:
            for dec in getattr(b, 'decorators', []) or []:
                if dec not in rv.decorators:
                    rv.decorators += (dec,)

        if 'decorators' in d:
            rv.decorators += d['decorators']

        return rv


class Resource(MethodView):
    """Base resource class"""

    def __new__(cls, *args, **kwargs):
        """Constructor of a resource instance"""
        if hasattr(cls, '_data_layer'):
            cls._data_layer.resource = cls

        return super(Resource, cls).__new__(cls)

    def dispatch_request(self, *args, **kwargs):
        """Logic of how to handle a request"""
        method = getattr(self, request.method.lower(), None)
        if method is None and request.method == 'HEAD':
            method = getattr(self, 'get', None)
        assert method is not None, 'Unimplemented method {}'.format(request.method)

        headers = {'Content-Type': 'application/vnd.api+json'}

        response = method(*args, **kwargs)

        if isinstance(response, Response):
            if "Content-Type" not in response.headers:
                response.headers.add('Content-Type', 'application/vnd.api+json')
            return response

        if not isinstance(response, tuple):
            if isinstance(response, dict):
                response.update({'jsonapi': {'version': '1.0'}})
            return make_response(json_dumps(response), 200, headers)

        try:
            data, status_code, headers = response
            if "Content-Type" not in headers:
                headers.update({'Content-Type': 'application/vnd.api+json'})
        except ValueError:
            pass

        try:
            data, status_code = response
        except ValueError:
            pass

        if isinstance(data, dict):
            data.update({'jsonapi': {'version': '1.0'}})

        if isinstance(data, FlaskResponse):
            if "Content-Type" not in data.headers:
                data.headers.add('Content-Type', 'application/vnd.api+json')
            data.status_code = status_code
            return data
        elif isinstance(data, str):
            json_reponse = data
        else:
            json_reponse = json_dumps(data)

        return make_response(json_reponse, status_code, headers)


class ResourceList(with_metaclass(ResourceMeta, Resource)):
    """Base class of a resource list manager"""

    @check_method_requirements
    def get(self, *args, **kwargs):
        """Retrieve a collection of objects"""
        self.before_get(args, kwargs)

        qs = QSManager(request.args, self.schema)

        parent_filter = self._get_parent_filter(request.url, kwargs)
        objects_count, objects = self.get_collection(qs, kwargs, filters=parent_filter)

        schema_kwargs = getattr(self, 'get_schema_kwargs', dict())
        schema_kwargs.update({'many': True})

        self.before_marshmallow(args, kwargs)

        schema = compute_schema(self.schema,
                                schema_kwargs,
                                qs,
                                qs.include)

        result = schema.dump(objects)

        view_kwargs = request.view_args if getattr(self, 'view_kwargs', None) is True else dict()
        add_pagination_links(result,
                             objects_count,
                             qs,
                             url_for(self.view, _external=True, **view_kwargs))

        result.update({'meta': {'count': objects_count}})

        final_result = self.after_get(result)

        return final_result

    @check_method_requirements
    def post(self, *args, **kwargs):
        """Create an object"""
        json_data = request.get_json() or {}

        qs = QSManager(request.args, self.schema)

        self.before_marshmallow(args, kwargs)

        schema = compute_schema(getattr(self, 'post_schema', self.schema),
                                getattr(self, 'post_schema_kwargs', dict()),
                                qs,
                                qs.include)

        data = schema.load(json_data)

        self.before_post(args, kwargs, data=data)

        try:
            obj = self.create_object(data, kwargs)
        except Exception:
            # Subclass can override self.create_object, but doesn't have to do it
            # correctly. Let's protect from that.
            self._data_layer.rollback()
            raise

        result = getattr(self, 'post_response_schema', self.schema)(many=False).dump(obj)

        if result['data'].get('links', {}).get('self'):
            final_result = (result, 201, {'Location': result['data']['links']['self']})
        else:
            final_result = (result, 201)

        result = self.after_post(final_result)

        return result

    def _get_parent_filter(self, url, kwargs):
        """
        Returns a dictionary of filters that should be applied to ensure only resources
        belonging to the parent resource are returned
        """

        url_segments = url.split('/')
        parent_segment = url_segments[-3]
        parent_id = url_segments[-2]

        for key, value in self.schema._declared_fields.items():
            if isinstance(value, BaseRelationship):
                if value.type_ == parent_segment:
                    return {value.id_field: parent_id}

        return {}

    def before_get(self, args, kwargs):
        """Hook to make custom work before get method"""
        pass

    def after_get(self, result):
        """Hook to make custom work after get method"""
        return result

    def before_post(self, args, kwargs, data=None):
        """Hook to make custom work before post method"""
        pass

    def after_post(self, result):
        """Hook to make custom work after post method"""
        return result

    def before_marshmallow(self, args, kwargs):
        pass

    def get_collection(self, qs, kwargs, filters=None):
        """
        Implements override for ResourceList that allows lists as
        values for simple filters, ie. following query strings are supported:
        ?filter[foobar_id]=1,2,3
        """

        request_args = ImmutableMultiDict(
            self._transform_simple_filter(k, v) for k, v in qs.qs.items(multi=True)
        )

        qs = QSManager(request_args, self.schema)

        return self._data_layer.get_collection(qs, kwargs, filters=filters)

    _RE_IS_SIMPLE_FILTER = re.compile(r"^filter\[([A-Za-z_-]+)\]$")
    _RE_IS_LIST_VALUE = re.compile(r"^\[(.+)\]$")

    def _transform_simple_filter(self, k, v):
        key_match = self._RE_IS_SIMPLE_FILTER.match(k)
        value_match = self._RE_IS_LIST_VALUE.match(v)

        if key_match and value_match:
            k = 'filter'

            try:
                values = [int(_) for _ in value_match.groups()[0].split(',')]

            except ValueError:
                values = value_match.groups()[0].split(',')

            v = json_dumps([{'name': key_match.groups()[0], 'op': 'in', 'val': values}])

        return k, v

    def create_object(self, data, kwargs):
        return self._data_layer.create_object(data, kwargs)


class ResourceDetail(with_metaclass(ResourceMeta, Resource)):
    """Base class of a resource detail manager"""

    @check_method_requirements
    def get(self, *args, **kwargs):
        """Get object details"""
        self.before_get(args, kwargs)

        qs = QSManager(request.args, self.schema)

        obj = self.get_object(kwargs, qs)

        self.before_marshmallow(args, kwargs)

        schema = compute_schema(self.schema,
                                getattr(self, 'get_schema_kwargs', dict()),
                                qs,
                                qs.include)

        result = schema.dump(obj) if obj else None

        final_result = self.after_get(result)

        return final_result

    @check_method_requirements
    def patch(self, *args, **kwargs):
        """Update an object"""
        json_data = request.get_json() or {}

        qs = QSManager(request.args, self.schema)
        schema_kwargs = getattr(self, 'patch_schema_kwargs', dict())
        schema_kwargs.update({'partial': True})

        self.before_marshmallow(args, kwargs)

        schema = compute_schema(getattr(self, 'patch_schema', self.schema),
                                schema_kwargs,
                                qs,
                                qs.include)

        data = schema.load(json_data)

        if 'id' not in json_data['data']:
            raise BadRequest('Missing id in "data" node',
                             source={'pointer': '/data/id'})
        if (str(json_data['data']['id']) != str(kwargs[getattr(self._data_layer, 'url_field', 'id')])):
            raise BadRequest('Value of id does not match the resource identifier in url',
                             source={'pointer': '/data/id'})

        self.before_patch(args, kwargs, data=data)

        try:
            obj = self.update_object(data, qs, kwargs)
        except Exception:
            self._data_layer.rollback()
            raise

        result = getattr(self, 'patch_response_schema', self.schema)(many=False).dump(obj)

        final_result = self.after_patch(result)

        return final_result

    @check_method_requirements
    def delete(self, *args, **kwargs):
        """Delete an object"""
        self.before_delete(args, kwargs)

        self.delete_object(kwargs)

        result = {'meta': {'message': 'Object successfully deleted'}}

        final_result = self.after_delete(result)

        return final_result

    def before_get(self, args, kwargs):
        """Hook to make custom work before get method"""
        pass

    def after_get(self, result):
        """Hook to make custom work after get method"""
        return result

    def before_patch(self, args, kwargs, data=None):
        """Hook to make custom work before patch method"""
        pass

    def after_patch(self, result):
        """Hook to make custom work after patch method"""
        return result

    def before_delete(self, args, kwargs):
        """Hook to make custom work before delete method"""
        pass

    def after_delete(self, result):
        """Hook to make custom work after delete method"""
        return result

    def before_marshmallow(self, args, kwargs):
        pass

    def get_object(self, kwargs, qs):
        return self._data_layer.get_object(kwargs, qs=qs)

    def update_object(self, data, qs, kwargs):
        obj = self._data_layer.get_object(kwargs, qs=qs)
        self._data_layer.update_object(obj, data, kwargs)

        return obj

    def delete_object(self, kwargs):
        obj = self._data_layer.get_object(kwargs)
        self._data_layer.delete_object(obj, kwargs)


class ResourceRelationship(with_metaclass(ResourceMeta, Resource)):
    """Base class of a resource relationship manager"""

    @check_method_requirements
    def get(self, *args, **kwargs):
        """Get a relationship details"""
        self.before_get(args, kwargs)

        relationship_field, model_relationship_field, related_type_, related_id_field = self._get_relationship_data()

        obj, data = self._data_layer.get_relationship(model_relationship_field,
                                                      related_type_,
                                                      related_id_field,
                                                      kwargs)

        result = {'links': {'self': request.path,
                            'related': self.schema._declared_fields[relationship_field].get_related_url(obj)},
                  'data': data}

        qs = QSManager(request.args, self.schema)
        if qs.include:
            schema = compute_schema(self.schema, dict(), qs, qs.include)

            serialized_obj = schema.dump(obj)
            result['included'] = serialized_obj.get('included', dict())

        final_result = self.after_get(result)

        return final_result

    @check_method_requirements
    def post(self, *args, **kwargs):
        """Add / create relationship(s)"""
        json_data = request.get_json() or {}

        relationship_field, model_relationship_field, related_type_, related_id_field = self._get_relationship_data()

        if 'data' not in json_data:
            raise BadRequest('You must provide data with a "data" route node', source={'pointer': '/data'})
        if isinstance(json_data['data'], dict):
            if 'type' not in json_data['data']:
                raise BadRequest('Missing type in "data" node', source={'pointer': '/data/type'})
            if 'id' not in json_data['data']:
                raise BadRequest('Missing id in "data" node', source={'pointer': '/data/id'})
            if json_data['data']['type'] != related_type_:
                raise InvalidType('The type field does not match the resource type', source={'pointer': '/data/type'})
        if isinstance(json_data['data'], list):
            for obj in json_data['data']:
                if 'type' not in obj:
                    raise BadRequest('Missing type in "data" node', source={'pointer': '/data/type'})
                if 'id' not in obj:
                    raise BadRequest('Missing id in "data" node', source={'pointer': '/data/id'})
                if obj['type'] != related_type_:
                    raise InvalidType('The type provided does not match the resource type',
                                      source={'pointer': '/data/type'})

        self.before_post(args, kwargs, json_data=json_data)

        obj_, updated = self._data_layer.create_relationship(json_data,
                                                             model_relationship_field,
                                                             related_id_field,
                                                             kwargs)

        status_code = 200
        result = {'meta': {'message': 'Relationship successfully created'}}

        if updated is False:
            result = ''
            status_code = 204

        final_result = self.after_post(result, status_code)

        return final_result

    @check_method_requirements
    def patch(self, *args, **kwargs):
        """Update a relationship"""
        json_data = request.get_json() or {}

        relationship_field, model_relationship_field, related_type_, related_id_field = self._get_relationship_data()

        if 'data' not in json_data:
            raise BadRequest('You must provide data with a "data" route node', source={'pointer': '/data'})
        if isinstance(json_data['data'], dict):
            if 'type' not in json_data['data']:
                raise BadRequest('Missing type in "data" node', source={'pointer': '/data/type'})
            if 'id' not in json_data['data']:
                raise BadRequest('Missing id in "data" node', source={'pointer': '/data/id'})
            if json_data['data']['type'] != related_type_:
                raise InvalidType('The type field does not match the resource type', source={'pointer': '/data/type'})
        if isinstance(json_data['data'], list):
            for obj in json_data['data']:
                if 'type' not in obj:
                    raise BadRequest('Missing type in "data" node', source={'pointer': '/data/type'})
                if 'id' not in obj:
                    raise BadRequest('Missing id in "data" node', source={'pointer': '/data/id'})
                if obj['type'] != related_type_:
                    raise InvalidType('The type provided does not match the resource type',
                                      source={'pointer': '/data/type'})

        self.before_patch(args, kwargs, json_data=json_data)

        obj_, updated = self._data_layer.update_relationship(json_data,
                                                             model_relationship_field,
                                                             related_id_field,
                                                             kwargs)

        status_code = 200
        result = {'meta': {'message': 'Relationship successfully updated'}}

        if updated is False:
            result = ''
            status_code = 204

        final_result = self.after_patch(result, status_code)

        return final_result

    @check_method_requirements
    def delete(self, *args, **kwargs):
        """Delete relationship(s)"""
        json_data = request.get_json() or {}

        relationship_field, model_relationship_field, related_type_, related_id_field = self._get_relationship_data()

        if 'data' not in json_data:
            raise BadRequest('You must provide data with a "data" route node', source={'pointer': '/data'})
        if isinstance(json_data['data'], dict):
            if 'type' not in json_data['data']:
                raise BadRequest('Missing type in "data" node', source={'pointer': '/data/type'})
            if 'id' not in json_data['data']:
                raise BadRequest('Missing id in "data" node', source={'pointer': '/data/id'})
            if json_data['data']['type'] != related_type_:
                raise InvalidType('The type field does not match the resource type', source={'pointer': '/data/type'})
        if isinstance(json_data['data'], list):
            for obj in json_data['data']:
                if 'type' not in obj:
                    raise BadRequest('Missing type in "data" node', source={'pointer': '/data/type'})
                if 'id' not in obj:
                    raise BadRequest('Missing id in "data" node', source={'pointer': '/data/id'})
                if obj['type'] != related_type_:
                    raise InvalidType('The type provided does not match the resource type',
                                      source={'pointer': '/data/type'})

        self.before_delete(args, kwargs, json_data=json_data)

        obj_, updated = self._data_layer.delete_relationship(json_data,
                                                             model_relationship_field,
                                                             related_id_field,
                                                             kwargs)

        status_code = 200
        result = {'meta': {'message': 'Relationship successfully updated'}}

        if updated is False:
            result = ''
            status_code = 204

        final_result = self.after_delete(result, status_code)

        return final_result

    def _get_relationship_data(self):
        """Get useful data for relationship management"""
        relationship_field = request.path.split('/')[-1].replace('-', '_')

        if relationship_field not in get_relationships(self.schema):
            raise RelationNotFound("{} has no attribute {}".format(self.schema.__name__, relationship_field))

        related_type_ = self.schema._declared_fields[relationship_field].type_
        related_id_field = self.schema._declared_fields[relationship_field].id_field
        model_relationship_field = get_model_field(self.schema, relationship_field)

        return relationship_field, model_relationship_field, related_type_, related_id_field

    def before_get(self, args, kwargs):
        """Hook to make custom work before get method"""
        pass

    def after_get(self, result):
        """Hook to make custom work after get method"""
        return result

    def before_post(self, args, kwargs, json_data=None):
        """Hook to make custom work before post method"""
        pass

    def after_post(self, result, status_code):
        """Hook to make custom work after post method"""
        return result, status_code

    def before_patch(self, args, kwargs, json_data=None):
        """Hook to make custom work before patch method"""
        pass

    def after_patch(self, result, status_code):
        """Hook to make custom work after patch method"""
        return result, status_code

    def before_delete(self, args, kwargs, json_data=None):
        """Hook to make custom work before delete method"""
        pass

    def after_delete(self, result, status_code):
        """Hook to make custom work after delete method"""
        return result, status_code

# fmt: on
