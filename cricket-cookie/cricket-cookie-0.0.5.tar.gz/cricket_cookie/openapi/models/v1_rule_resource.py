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


class V1RuleResource(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    allowed enum values
    """
    UNSPECIFIEDRESOURCE = "unspecifiedResource"
    PROJECT = "project"
    PROJECTBILLING = "projectBilling"
    ROLE = "role"
    MEMBERSHIP = "membership"
    MEMBERSHIPROLEBINDING = "membershipRoleBinding"
    PROJECTCLUSTERBINDING = "projectClusterBinding"
    SESSION = "session"
    EXPERIMENT = "experiment"
    RUN = "run"
    DATASTORE = "datastore"
    ANY = "any"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}

    attribute_map = {}

    def __init__(self, _configuration=None):  # noqa: E501
        """V1RuleResource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration
        self.discriminator = None

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
        if issubclass(V1RuleResource, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'V1RuleResource') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, V1RuleResource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other: 'V1RuleResource') -> bool:
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1RuleResource):
            return True

        return self.to_dict() != other.to_dict()
