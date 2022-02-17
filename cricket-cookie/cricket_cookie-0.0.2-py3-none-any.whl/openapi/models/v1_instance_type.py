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


class V1InstanceType(object):
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
        'availability': 'InstanceTypeAvailability',
        'cpu': 'str',
        'gpu': 'str',
        'hourly_cost': 'float',
        'memory': 'str',
        'name': 'str',
        'overprovisioned_ondemand_count': 'int',
        'spot': 'bool'
    }

    attribute_map = {
        'availability': 'availability',
        'cpu': 'cpu',
        'gpu': 'gpu',
        'hourly_cost': 'hourlyCost',
        'memory': 'memory',
        'name': 'name',
        'overprovisioned_ondemand_count': 'overprovisionedOndemandCount',
        'spot': 'spot'
    }

    def __init__(self,
                 availability: 'InstanceTypeAvailability' = None,
                 cpu: 'str' = None,
                 gpu: 'str' = None,
                 hourly_cost: 'float' = None,
                 memory: 'str' = None,
                 name: 'str' = None,
                 overprovisioned_ondemand_count: 'int' = None,
                 spot: 'bool' = None,
                 _configuration=None):  # noqa: E501
        """V1InstanceType - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._availability = None
        self._cpu = None
        self._gpu = None
        self._hourly_cost = None
        self._memory = None
        self._name = None
        self._overprovisioned_ondemand_count = None
        self._spot = None
        self.discriminator = None

        if availability is not None:
            self.availability = availability
        if cpu is not None:
            self.cpu = cpu
        if gpu is not None:
            self.gpu = gpu
        if hourly_cost is not None:
            self.hourly_cost = hourly_cost
        if memory is not None:
            self.memory = memory
        if name is not None:
            self.name = name
        if overprovisioned_ondemand_count is not None:
            self.overprovisioned_ondemand_count = overprovisioned_ondemand_count
        if spot is not None:
            self.spot = spot

    @property
    def availability(self) -> 'InstanceTypeAvailability':
        """Gets the availability of this V1InstanceType.  # noqa: E501


        :return: The availability of this V1InstanceType.  # noqa: E501
        :rtype: InstanceTypeAvailability
        """
        return self._availability

    @availability.setter
    def availability(self, availability: 'InstanceTypeAvailability'):
        """Sets the availability of this V1InstanceType.


        :param availability: The availability of this V1InstanceType.  # noqa: E501
        :type: InstanceTypeAvailability
        """

        self._availability = availability

    @property
    def cpu(self) -> 'str':
        """Gets the cpu of this V1InstanceType.  # noqa: E501


        :return: The cpu of this V1InstanceType.  # noqa: E501
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu: 'str'):
        """Sets the cpu of this V1InstanceType.


        :param cpu: The cpu of this V1InstanceType.  # noqa: E501
        :type: str
        """

        self._cpu = cpu

    @property
    def gpu(self) -> 'str':
        """Gets the gpu of this V1InstanceType.  # noqa: E501


        :return: The gpu of this V1InstanceType.  # noqa: E501
        :rtype: str
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu: 'str'):
        """Sets the gpu of this V1InstanceType.


        :param gpu: The gpu of this V1InstanceType.  # noqa: E501
        :type: str
        """

        self._gpu = gpu

    @property
    def hourly_cost(self) -> 'float':
        """Gets the hourly_cost of this V1InstanceType.  # noqa: E501


        :return: The hourly_cost of this V1InstanceType.  # noqa: E501
        :rtype: float
        """
        return self._hourly_cost

    @hourly_cost.setter
    def hourly_cost(self, hourly_cost: 'float'):
        """Sets the hourly_cost of this V1InstanceType.


        :param hourly_cost: The hourly_cost of this V1InstanceType.  # noqa: E501
        :type: float
        """

        self._hourly_cost = hourly_cost

    @property
    def memory(self) -> 'str':
        """Gets the memory of this V1InstanceType.  # noqa: E501


        :return: The memory of this V1InstanceType.  # noqa: E501
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory: 'str'):
        """Sets the memory of this V1InstanceType.


        :param memory: The memory of this V1InstanceType.  # noqa: E501
        :type: str
        """

        self._memory = memory

    @property
    def name(self) -> 'str':
        """Gets the name of this V1InstanceType.  # noqa: E501


        :return: The name of this V1InstanceType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: 'str'):
        """Sets the name of this V1InstanceType.


        :param name: The name of this V1InstanceType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def overprovisioned_ondemand_count(self) -> 'int':
        """Gets the overprovisioned_ondemand_count of this V1InstanceType.  # noqa: E501


        :return: The overprovisioned_ondemand_count of this V1InstanceType.  # noqa: E501
        :rtype: int
        """
        return self._overprovisioned_ondemand_count

    @overprovisioned_ondemand_count.setter
    def overprovisioned_ondemand_count(self,
                                       overprovisioned_ondemand_count: 'int'):
        """Sets the overprovisioned_ondemand_count of this V1InstanceType.


        :param overprovisioned_ondemand_count: The overprovisioned_ondemand_count of this V1InstanceType.  # noqa: E501
        :type: int
        """

        self._overprovisioned_ondemand_count = overprovisioned_ondemand_count

    @property
    def spot(self) -> 'bool':
        """Gets the spot of this V1InstanceType.  # noqa: E501


        :return: The spot of this V1InstanceType.  # noqa: E501
        :rtype: bool
        """
        return self._spot

    @spot.setter
    def spot(self, spot: 'bool'):
        """Sets the spot of this V1InstanceType.


        :param spot: The spot of this V1InstanceType.  # noqa: E501
        :type: bool
        """

        self._spot = spot

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
        if issubclass(V1InstanceType, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'V1InstanceType') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, V1InstanceType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other: 'V1InstanceType') -> bool:
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1InstanceType):
            return True

        return self.to_dict() != other.to_dict()
