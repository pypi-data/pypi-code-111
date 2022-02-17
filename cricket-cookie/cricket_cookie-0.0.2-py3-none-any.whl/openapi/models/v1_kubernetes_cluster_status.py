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


class V1KubernetesClusterStatus(object):
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
        'azure': 'V1AzureClusterDriverStatus',
        'bastion_host_ip': 'str',
        'eks': 'V1EKSCusterDriverStatus',
        'ingress_ca_cert': 'str',
        'ingress_load_balancer_hostname': 'str',
        'ingress_load_balancer_ip': 'str',
        'monitoring_client_cert': 'str',
        'monitoring_client_key': 'str',
        'ssh_private_key': 'str',
        'ssh_public_key': 'str'
    }

    attribute_map = {
        'azure': 'azure',
        'bastion_host_ip': 'bastionHostIp',
        'eks': 'eks',
        'ingress_ca_cert': 'ingressCaCert',
        'ingress_load_balancer_hostname': 'ingressLoadBalancerHostname',
        'ingress_load_balancer_ip': 'ingressLoadBalancerIp',
        'monitoring_client_cert': 'monitoringClientCert',
        'monitoring_client_key': 'monitoringClientKey',
        'ssh_private_key': 'sshPrivateKey',
        'ssh_public_key': 'sshPublicKey'
    }

    def __init__(self,
                 azure: 'V1AzureClusterDriverStatus' = None,
                 bastion_host_ip: 'str' = None,
                 eks: 'V1EKSCusterDriverStatus' = None,
                 ingress_ca_cert: 'str' = None,
                 ingress_load_balancer_hostname: 'str' = None,
                 ingress_load_balancer_ip: 'str' = None,
                 monitoring_client_cert: 'str' = None,
                 monitoring_client_key: 'str' = None,
                 ssh_private_key: 'str' = None,
                 ssh_public_key: 'str' = None,
                 _configuration=None):  # noqa: E501
        """V1KubernetesClusterStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._azure = None
        self._bastion_host_ip = None
        self._eks = None
        self._ingress_ca_cert = None
        self._ingress_load_balancer_hostname = None
        self._ingress_load_balancer_ip = None
        self._monitoring_client_cert = None
        self._monitoring_client_key = None
        self._ssh_private_key = None
        self._ssh_public_key = None
        self.discriminator = None

        if azure is not None:
            self.azure = azure
        if bastion_host_ip is not None:
            self.bastion_host_ip = bastion_host_ip
        if eks is not None:
            self.eks = eks
        if ingress_ca_cert is not None:
            self.ingress_ca_cert = ingress_ca_cert
        if ingress_load_balancer_hostname is not None:
            self.ingress_load_balancer_hostname = ingress_load_balancer_hostname
        if ingress_load_balancer_ip is not None:
            self.ingress_load_balancer_ip = ingress_load_balancer_ip
        if monitoring_client_cert is not None:
            self.monitoring_client_cert = monitoring_client_cert
        if monitoring_client_key is not None:
            self.monitoring_client_key = monitoring_client_key
        if ssh_private_key is not None:
            self.ssh_private_key = ssh_private_key
        if ssh_public_key is not None:
            self.ssh_public_key = ssh_public_key

    @property
    def azure(self) -> 'V1AzureClusterDriverStatus':
        """Gets the azure of this V1KubernetesClusterStatus.  # noqa: E501


        :return: The azure of this V1KubernetesClusterStatus.  # noqa: E501
        :rtype: V1AzureClusterDriverStatus
        """
        return self._azure

    @azure.setter
    def azure(self, azure: 'V1AzureClusterDriverStatus'):
        """Sets the azure of this V1KubernetesClusterStatus.


        :param azure: The azure of this V1KubernetesClusterStatus.  # noqa: E501
        :type: V1AzureClusterDriverStatus
        """

        self._azure = azure

    @property
    def bastion_host_ip(self) -> 'str':
        """Gets the bastion_host_ip of this V1KubernetesClusterStatus.  # noqa: E501


        :return: The bastion_host_ip of this V1KubernetesClusterStatus.  # noqa: E501
        :rtype: str
        """
        return self._bastion_host_ip

    @bastion_host_ip.setter
    def bastion_host_ip(self, bastion_host_ip: 'str'):
        """Sets the bastion_host_ip of this V1KubernetesClusterStatus.


        :param bastion_host_ip: The bastion_host_ip of this V1KubernetesClusterStatus.  # noqa: E501
        :type: str
        """

        self._bastion_host_ip = bastion_host_ip

    @property
    def eks(self) -> 'V1EKSCusterDriverStatus':
        """Gets the eks of this V1KubernetesClusterStatus.  # noqa: E501


        :return: The eks of this V1KubernetesClusterStatus.  # noqa: E501
        :rtype: V1EKSCusterDriverStatus
        """
        return self._eks

    @eks.setter
    def eks(self, eks: 'V1EKSCusterDriverStatus'):
        """Sets the eks of this V1KubernetesClusterStatus.


        :param eks: The eks of this V1KubernetesClusterStatus.  # noqa: E501
        :type: V1EKSCusterDriverStatus
        """

        self._eks = eks

    @property
    def ingress_ca_cert(self) -> 'str':
        """Gets the ingress_ca_cert of this V1KubernetesClusterStatus.  # noqa: E501


        :return: The ingress_ca_cert of this V1KubernetesClusterStatus.  # noqa: E501
        :rtype: str
        """
        return self._ingress_ca_cert

    @ingress_ca_cert.setter
    def ingress_ca_cert(self, ingress_ca_cert: 'str'):
        """Sets the ingress_ca_cert of this V1KubernetesClusterStatus.


        :param ingress_ca_cert: The ingress_ca_cert of this V1KubernetesClusterStatus.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation
                and ingress_ca_cert is not None and not re.search(
                    r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$',
                    ingress_ca_cert)):  # noqa: E501
            raise ValueError(
                r"Invalid value for `ingress_ca_cert`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`"
            )  # noqa: E501

        self._ingress_ca_cert = ingress_ca_cert

    @property
    def ingress_load_balancer_hostname(self) -> 'str':
        """Gets the ingress_load_balancer_hostname of this V1KubernetesClusterStatus.  # noqa: E501


        :return: The ingress_load_balancer_hostname of this V1KubernetesClusterStatus.  # noqa: E501
        :rtype: str
        """
        return self._ingress_load_balancer_hostname

    @ingress_load_balancer_hostname.setter
    def ingress_load_balancer_hostname(self,
                                       ingress_load_balancer_hostname: 'str'):
        """Sets the ingress_load_balancer_hostname of this V1KubernetesClusterStatus.


        :param ingress_load_balancer_hostname: The ingress_load_balancer_hostname of this V1KubernetesClusterStatus.  # noqa: E501
        :type: str
        """

        self._ingress_load_balancer_hostname = ingress_load_balancer_hostname

    @property
    def ingress_load_balancer_ip(self) -> 'str':
        """Gets the ingress_load_balancer_ip of this V1KubernetesClusterStatus.  # noqa: E501


        :return: The ingress_load_balancer_ip of this V1KubernetesClusterStatus.  # noqa: E501
        :rtype: str
        """
        return self._ingress_load_balancer_ip

    @ingress_load_balancer_ip.setter
    def ingress_load_balancer_ip(self, ingress_load_balancer_ip: 'str'):
        """Sets the ingress_load_balancer_ip of this V1KubernetesClusterStatus.


        :param ingress_load_balancer_ip: The ingress_load_balancer_ip of this V1KubernetesClusterStatus.  # noqa: E501
        :type: str
        """

        self._ingress_load_balancer_ip = ingress_load_balancer_ip

    @property
    def monitoring_client_cert(self) -> 'str':
        """Gets the monitoring_client_cert of this V1KubernetesClusterStatus.  # noqa: E501


        :return: The monitoring_client_cert of this V1KubernetesClusterStatus.  # noqa: E501
        :rtype: str
        """
        return self._monitoring_client_cert

    @monitoring_client_cert.setter
    def monitoring_client_cert(self, monitoring_client_cert: 'str'):
        """Sets the monitoring_client_cert of this V1KubernetesClusterStatus.


        :param monitoring_client_cert: The monitoring_client_cert of this V1KubernetesClusterStatus.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation
                and monitoring_client_cert is not None and not re.search(
                    r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$',
                    monitoring_client_cert)):  # noqa: E501
            raise ValueError(
                r"Invalid value for `monitoring_client_cert`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`"
            )  # noqa: E501

        self._monitoring_client_cert = monitoring_client_cert

    @property
    def monitoring_client_key(self) -> 'str':
        """Gets the monitoring_client_key of this V1KubernetesClusterStatus.  # noqa: E501


        :return: The monitoring_client_key of this V1KubernetesClusterStatus.  # noqa: E501
        :rtype: str
        """
        return self._monitoring_client_key

    @monitoring_client_key.setter
    def monitoring_client_key(self, monitoring_client_key: 'str'):
        """Sets the monitoring_client_key of this V1KubernetesClusterStatus.


        :param monitoring_client_key: The monitoring_client_key of this V1KubernetesClusterStatus.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation
                and monitoring_client_key is not None and not re.search(
                    r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$',
                    monitoring_client_key)):  # noqa: E501
            raise ValueError(
                r"Invalid value for `monitoring_client_key`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`"
            )  # noqa: E501

        self._monitoring_client_key = monitoring_client_key

    @property
    def ssh_private_key(self) -> 'str':
        """Gets the ssh_private_key of this V1KubernetesClusterStatus.  # noqa: E501


        :return: The ssh_private_key of this V1KubernetesClusterStatus.  # noqa: E501
        :rtype: str
        """
        return self._ssh_private_key

    @ssh_private_key.setter
    def ssh_private_key(self, ssh_private_key: 'str'):
        """Sets the ssh_private_key of this V1KubernetesClusterStatus.


        :param ssh_private_key: The ssh_private_key of this V1KubernetesClusterStatus.  # noqa: E501
        :type: str
        """

        self._ssh_private_key = ssh_private_key

    @property
    def ssh_public_key(self) -> 'str':
        """Gets the ssh_public_key of this V1KubernetesClusterStatus.  # noqa: E501


        :return: The ssh_public_key of this V1KubernetesClusterStatus.  # noqa: E501
        :rtype: str
        """
        return self._ssh_public_key

    @ssh_public_key.setter
    def ssh_public_key(self, ssh_public_key: 'str'):
        """Sets the ssh_public_key of this V1KubernetesClusterStatus.


        :param ssh_public_key: The ssh_public_key of this V1KubernetesClusterStatus.  # noqa: E501
        :type: str
        """

        self._ssh_public_key = ssh_public_key

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
        if issubclass(V1KubernetesClusterStatus, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'V1KubernetesClusterStatus') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, V1KubernetesClusterStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other: 'V1KubernetesClusterStatus') -> bool:
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1KubernetesClusterStatus):
            return True

        return self.to_dict() != other.to_dict()
