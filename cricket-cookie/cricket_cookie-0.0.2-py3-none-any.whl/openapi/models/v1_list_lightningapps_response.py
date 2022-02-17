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


class V1ListLightningappsResponse(object):
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
        'lightningapps': 'list[Externalv1Lightningapp]',
        'next_page_token': 'str',
        'previous_page_token': 'str'
    }

    attribute_map = {
        'lightningapps': 'lightningapps',
        'next_page_token': 'nextPageToken',
        'previous_page_token': 'previousPageToken'
    }

    def __init__(self,
                 lightningapps: 'list[Externalv1Lightningapp]' = None,
                 next_page_token: 'str' = None,
                 previous_page_token: 'str' = None,
                 _configuration=None):  # noqa: E501
        """V1ListLightningappsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._lightningapps = None
        self._next_page_token = None
        self._previous_page_token = None
        self.discriminator = None

        if lightningapps is not None:
            self.lightningapps = lightningapps
        if next_page_token is not None:
            self.next_page_token = next_page_token
        if previous_page_token is not None:
            self.previous_page_token = previous_page_token

    @property
    def lightningapps(self) -> 'list[Externalv1Lightningapp]':
        """Gets the lightningapps of this V1ListLightningappsResponse.  # noqa: E501


        :return: The lightningapps of this V1ListLightningappsResponse.  # noqa: E501
        :rtype: list[Externalv1Lightningapp]
        """
        return self._lightningapps

    @lightningapps.setter
    def lightningapps(self, lightningapps: 'list[Externalv1Lightningapp]'):
        """Sets the lightningapps of this V1ListLightningappsResponse.


        :param lightningapps: The lightningapps of this V1ListLightningappsResponse.  # noqa: E501
        :type: list[Externalv1Lightningapp]
        """

        self._lightningapps = lightningapps

    @property
    def next_page_token(self) -> 'str':
        """Gets the next_page_token of this V1ListLightningappsResponse.  # noqa: E501


        :return: The next_page_token of this V1ListLightningappsResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token: 'str'):
        """Sets the next_page_token of this V1ListLightningappsResponse.


        :param next_page_token: The next_page_token of this V1ListLightningappsResponse.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

    @property
    def previous_page_token(self) -> 'str':
        """Gets the previous_page_token of this V1ListLightningappsResponse.  # noqa: E501


        :return: The previous_page_token of this V1ListLightningappsResponse.  # noqa: E501
        :rtype: str
        """
        return self._previous_page_token

    @previous_page_token.setter
    def previous_page_token(self, previous_page_token: 'str'):
        """Sets the previous_page_token of this V1ListLightningappsResponse.


        :param previous_page_token: The previous_page_token of this V1ListLightningappsResponse.  # noqa: E501
        :type: str
        """

        self._previous_page_token = previous_page_token

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
        if issubclass(V1ListLightningappsResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'V1ListLightningappsResponse') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, V1ListLightningappsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other: 'V1ListLightningappsResponse') -> bool:
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ListLightningappsResponse):
            return True

        return self.to_dict() != other.to_dict()
