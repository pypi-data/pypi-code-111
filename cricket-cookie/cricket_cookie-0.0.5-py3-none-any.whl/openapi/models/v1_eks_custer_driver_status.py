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


class V1EKSCusterDriverStatus(object):
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
        'bastion_ami': 'str',
        'builder_ami': 'str',
        'cpu_ami': 'str',
        'ecr_registry_id': 'str',
        'ecr_repository_uri': 'str',
        'gpu_ami': 'str',
        'gridlet_role_arn': 'str',
        'user_workload_role_arn': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'bastion_ami': 'bastionAmi',
        'builder_ami': 'builderAmi',
        'cpu_ami': 'cpuAmi',
        'ecr_registry_id': 'ecrRegistryId',
        'ecr_repository_uri': 'ecrRepositoryUri',
        'gpu_ami': 'gpuAmi',
        'gridlet_role_arn': 'gridletRoleArn',
        'user_workload_role_arn': 'userWorkloadRoleArn',
        'vpc_id': 'vpcId'
    }

    def __init__(self,
                 bastion_ami: 'str' = None,
                 builder_ami: 'str' = None,
                 cpu_ami: 'str' = None,
                 ecr_registry_id: 'str' = None,
                 ecr_repository_uri: 'str' = None,
                 gpu_ami: 'str' = None,
                 gridlet_role_arn: 'str' = None,
                 user_workload_role_arn: 'str' = None,
                 vpc_id: 'str' = None,
                 _configuration=None):  # noqa: E501
        """V1EKSCusterDriverStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bastion_ami = None
        self._builder_ami = None
        self._cpu_ami = None
        self._ecr_registry_id = None
        self._ecr_repository_uri = None
        self._gpu_ami = None
        self._gridlet_role_arn = None
        self._user_workload_role_arn = None
        self._vpc_id = None
        self.discriminator = None

        if bastion_ami is not None:
            self.bastion_ami = bastion_ami
        if builder_ami is not None:
            self.builder_ami = builder_ami
        if cpu_ami is not None:
            self.cpu_ami = cpu_ami
        if ecr_registry_id is not None:
            self.ecr_registry_id = ecr_registry_id
        if ecr_repository_uri is not None:
            self.ecr_repository_uri = ecr_repository_uri
        if gpu_ami is not None:
            self.gpu_ami = gpu_ami
        if gridlet_role_arn is not None:
            self.gridlet_role_arn = gridlet_role_arn
        if user_workload_role_arn is not None:
            self.user_workload_role_arn = user_workload_role_arn
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def bastion_ami(self) -> 'str':
        """Gets the bastion_ami of this V1EKSCusterDriverStatus.  # noqa: E501


        :return: The bastion_ami of this V1EKSCusterDriverStatus.  # noqa: E501
        :rtype: str
        """
        return self._bastion_ami

    @bastion_ami.setter
    def bastion_ami(self, bastion_ami: 'str'):
        """Sets the bastion_ami of this V1EKSCusterDriverStatus.


        :param bastion_ami: The bastion_ami of this V1EKSCusterDriverStatus.  # noqa: E501
        :type: str
        """

        self._bastion_ami = bastion_ami

    @property
    def builder_ami(self) -> 'str':
        """Gets the builder_ami of this V1EKSCusterDriverStatus.  # noqa: E501


        :return: The builder_ami of this V1EKSCusterDriverStatus.  # noqa: E501
        :rtype: str
        """
        return self._builder_ami

    @builder_ami.setter
    def builder_ami(self, builder_ami: 'str'):
        """Sets the builder_ami of this V1EKSCusterDriverStatus.


        :param builder_ami: The builder_ami of this V1EKSCusterDriverStatus.  # noqa: E501
        :type: str
        """

        self._builder_ami = builder_ami

    @property
    def cpu_ami(self) -> 'str':
        """Gets the cpu_ami of this V1EKSCusterDriverStatus.  # noqa: E501

        AMI to be used for CPU nodes.  # noqa: E501

        :return: The cpu_ami of this V1EKSCusterDriverStatus.  # noqa: E501
        :rtype: str
        """
        return self._cpu_ami

    @cpu_ami.setter
    def cpu_ami(self, cpu_ami: 'str'):
        """Sets the cpu_ami of this V1EKSCusterDriverStatus.

        AMI to be used for CPU nodes.  # noqa: E501

        :param cpu_ami: The cpu_ami of this V1EKSCusterDriverStatus.  # noqa: E501
        :type: str
        """

        self._cpu_ami = cpu_ami

    @property
    def ecr_registry_id(self) -> 'str':
        """Gets the ecr_registry_id of this V1EKSCusterDriverStatus.  # noqa: E501


        :return: The ecr_registry_id of this V1EKSCusterDriverStatus.  # noqa: E501
        :rtype: str
        """
        return self._ecr_registry_id

    @ecr_registry_id.setter
    def ecr_registry_id(self, ecr_registry_id: 'str'):
        """Sets the ecr_registry_id of this V1EKSCusterDriverStatus.


        :param ecr_registry_id: The ecr_registry_id of this V1EKSCusterDriverStatus.  # noqa: E501
        :type: str
        """

        self._ecr_registry_id = ecr_registry_id

    @property
    def ecr_repository_uri(self) -> 'str':
        """Gets the ecr_repository_uri of this V1EKSCusterDriverStatus.  # noqa: E501


        :return: The ecr_repository_uri of this V1EKSCusterDriverStatus.  # noqa: E501
        :rtype: str
        """
        return self._ecr_repository_uri

    @ecr_repository_uri.setter
    def ecr_repository_uri(self, ecr_repository_uri: 'str'):
        """Sets the ecr_repository_uri of this V1EKSCusterDriverStatus.


        :param ecr_repository_uri: The ecr_repository_uri of this V1EKSCusterDriverStatus.  # noqa: E501
        :type: str
        """

        self._ecr_repository_uri = ecr_repository_uri

    @property
    def gpu_ami(self) -> 'str':
        """Gets the gpu_ami of this V1EKSCusterDriverStatus.  # noqa: E501

        AMI to be used for GPU nodes.  # noqa: E501

        :return: The gpu_ami of this V1EKSCusterDriverStatus.  # noqa: E501
        :rtype: str
        """
        return self._gpu_ami

    @gpu_ami.setter
    def gpu_ami(self, gpu_ami: 'str'):
        """Sets the gpu_ami of this V1EKSCusterDriverStatus.

        AMI to be used for GPU nodes.  # noqa: E501

        :param gpu_ami: The gpu_ami of this V1EKSCusterDriverStatus.  # noqa: E501
        :type: str
        """

        self._gpu_ami = gpu_ami

    @property
    def gridlet_role_arn(self) -> 'str':
        """Gets the gridlet_role_arn of this V1EKSCusterDriverStatus.  # noqa: E501


        :return: The gridlet_role_arn of this V1EKSCusterDriverStatus.  # noqa: E501
        :rtype: str
        """
        return self._gridlet_role_arn

    @gridlet_role_arn.setter
    def gridlet_role_arn(self, gridlet_role_arn: 'str'):
        """Sets the gridlet_role_arn of this V1EKSCusterDriverStatus.


        :param gridlet_role_arn: The gridlet_role_arn of this V1EKSCusterDriverStatus.  # noqa: E501
        :type: str
        """

        self._gridlet_role_arn = gridlet_role_arn

    @property
    def user_workload_role_arn(self) -> 'str':
        """Gets the user_workload_role_arn of this V1EKSCusterDriverStatus.  # noqa: E501


        :return: The user_workload_role_arn of this V1EKSCusterDriverStatus.  # noqa: E501
        :rtype: str
        """
        return self._user_workload_role_arn

    @user_workload_role_arn.setter
    def user_workload_role_arn(self, user_workload_role_arn: 'str'):
        """Sets the user_workload_role_arn of this V1EKSCusterDriverStatus.


        :param user_workload_role_arn: The user_workload_role_arn of this V1EKSCusterDriverStatus.  # noqa: E501
        :type: str
        """

        self._user_workload_role_arn = user_workload_role_arn

    @property
    def vpc_id(self) -> 'str':
        """Gets the vpc_id of this V1EKSCusterDriverStatus.  # noqa: E501


        :return: The vpc_id of this V1EKSCusterDriverStatus.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id: 'str'):
        """Sets the vpc_id of this V1EKSCusterDriverStatus.


        :param vpc_id: The vpc_id of this V1EKSCusterDriverStatus.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

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
        if issubclass(V1EKSCusterDriverStatus, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'V1EKSCusterDriverStatus') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, V1EKSCusterDriverStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other: 'V1EKSCusterDriverStatus') -> bool:
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1EKSCusterDriverStatus):
            return True

        return self.to_dict() != other.to_dict()
