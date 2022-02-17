# coding: utf-8
"""
    external/v1/auth_service.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set

    Generated by: https://github.com/swagger-api/swagger-codegen.git

    NOTE
    ----
    standard swagger-codegen-cli for this python client has been modified
    by custom templates. The purpose of these templates is to include
    typing information in the API and Model code. Please refer to the
    main grid repository for more info
"""

import pprint
import re  # noqa: F401
from typing import TYPE_CHECKING

import six

from cricket_cookie.openapi.configuration import Configuration

if TYPE_CHECKING:
    from datetime import datetime
    from cricket_cookie.openapi.models import *


class V1SearchUser(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'auth_provider': 'str',
        'first_name': 'str',
        'id': 'str',
        'last_name': 'str',
        'picture_url': 'str',
        'username': 'str'
    }

    attribute_map = {
        'auth_provider': 'authProvider',
        'first_name': 'firstName',
        'id': 'id',
        'last_name': 'lastName',
        'picture_url': 'pictureUrl',
        'username': 'username'
    }

    def __init__(self,
                 auth_provider: 'str' = None,
                 first_name: 'str' = None,
                 id: 'str' = None,
                 last_name: 'str' = None,
                 picture_url: 'str' = None,
                 username: 'str' = None,
                 _configuration=None):  # noqa: E501
        """V1SearchUser - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auth_provider = None
        self._first_name = None
        self._id = None
        self._last_name = None
        self._picture_url = None
        self._username = None
        self.discriminator = None

        if auth_provider is not None:
            self.auth_provider = auth_provider
        if first_name is not None:
            self.first_name = first_name
        if id is not None:
            self.id = id
        if last_name is not None:
            self.last_name = last_name
        if picture_url is not None:
            self.picture_url = picture_url
        if username is not None:
            self.username = username

    @property
    def auth_provider(self) -> 'str':
        """Gets the auth_provider of this V1SearchUser.  # noqa: E501


        :return: The auth_provider of this V1SearchUser.  # noqa: E501
        :rtype: str
        """
        return self._auth_provider

    @auth_provider.setter
    def auth_provider(self, auth_provider: 'str'):
        """Sets the auth_provider of this V1SearchUser.


        :param auth_provider: The auth_provider of this V1SearchUser.  # noqa: E501
        :type: str
        """

        self._auth_provider = auth_provider

    @property
    def first_name(self) -> 'str':
        """Gets the first_name of this V1SearchUser.  # noqa: E501


        :return: The first_name of this V1SearchUser.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: 'str'):
        """Sets the first_name of this V1SearchUser.


        :param first_name: The first_name of this V1SearchUser.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def id(self) -> 'str':
        """Gets the id of this V1SearchUser.  # noqa: E501


        :return: The id of this V1SearchUser.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: 'str'):
        """Sets the id of this V1SearchUser.


        :param id: The id of this V1SearchUser.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_name(self) -> 'str':
        """Gets the last_name of this V1SearchUser.  # noqa: E501


        :return: The last_name of this V1SearchUser.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: 'str'):
        """Sets the last_name of this V1SearchUser.


        :param last_name: The last_name of this V1SearchUser.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def picture_url(self) -> 'str':
        """Gets the picture_url of this V1SearchUser.  # noqa: E501


        :return: The picture_url of this V1SearchUser.  # noqa: E501
        :rtype: str
        """
        return self._picture_url

    @picture_url.setter
    def picture_url(self, picture_url: 'str'):
        """Sets the picture_url of this V1SearchUser.


        :param picture_url: The picture_url of this V1SearchUser.  # noqa: E501
        :type: str
        """

        self._picture_url = picture_url

    @property
    def username(self) -> 'str':
        """Gets the username of this V1SearchUser.  # noqa: E501


        :return: The username of this V1SearchUser.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: 'str'):
        """Sets the username of this V1SearchUser.


        :param username: The username of this V1SearchUser.  # noqa: E501
        :type: str
        """

        self._username = username

    def to_dict(self) -> dict:
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict()
                        if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()))
            else:
                result[attr] = value
        if issubclass(V1SearchUser, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'V1SearchUser') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, V1SearchUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other: 'V1SearchUser') -> bool:
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1SearchUser):
            return True

        return self.to_dict() != other.to_dict()
