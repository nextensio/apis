# coding: utf-8

"""
    Controller APIs

    APIs to act on Nextensio Controller  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: developer@nextensio.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TenantCluster(object):
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
        'id': 'str',
        'gateway': 'str',
        'image': 'str',
        'apodrepl': 'int',
        'apodsets': 'int'
    }

    attribute_map = {
        'id': 'id',
        'gateway': 'gateway',
        'image': 'image',
        'apodrepl': 'apodrepl',
        'apodsets': 'apodsets'
    }

    def __init__(self, id=None, gateway=None, image=None, apodrepl=None, apodsets=None):  # noqa: E501
        """TenantCluster - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._gateway = None
        self._image = None
        self._apodrepl = None
        self._apodsets = None
        self.discriminator = None
        self.id = id
        self.gateway = gateway
        self.image = image
        self.apodrepl = apodrepl
        self.apodsets = apodsets

    @property
    def id(self):
        """Gets the id of this TenantCluster.  # noqa: E501


        :return: The id of this TenantCluster.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TenantCluster.


        :param id: The id of this TenantCluster.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def gateway(self):
        """Gets the gateway of this TenantCluster.  # noqa: E501


        :return: The gateway of this TenantCluster.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this TenantCluster.


        :param gateway: The gateway of this TenantCluster.  # noqa: E501
        :type: str
        """
        if gateway is None:
            raise ValueError("Invalid value for `gateway`, must not be `None`")  # noqa: E501

        self._gateway = gateway

    @property
    def image(self):
        """Gets the image of this TenantCluster.  # noqa: E501


        :return: The image of this TenantCluster.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this TenantCluster.


        :param image: The image of this TenantCluster.  # noqa: E501
        :type: str
        """
        if image is None:
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501

        self._image = image

    @property
    def apodrepl(self):
        """Gets the apodrepl of this TenantCluster.  # noqa: E501


        :return: The apodrepl of this TenantCluster.  # noqa: E501
        :rtype: int
        """
        return self._apodrepl

    @apodrepl.setter
    def apodrepl(self, apodrepl):
        """Sets the apodrepl of this TenantCluster.


        :param apodrepl: The apodrepl of this TenantCluster.  # noqa: E501
        :type: int
        """
        if apodrepl is None:
            raise ValueError("Invalid value for `apodrepl`, must not be `None`")  # noqa: E501

        self._apodrepl = apodrepl

    @property
    def apodsets(self):
        """Gets the apodsets of this TenantCluster.  # noqa: E501


        :return: The apodsets of this TenantCluster.  # noqa: E501
        :rtype: int
        """
        return self._apodsets

    @apodsets.setter
    def apodsets(self, apodsets):
        """Sets the apodsets of this TenantCluster.


        :param apodsets: The apodsets of this TenantCluster.  # noqa: E501
        :type: int
        """
        if apodsets is None:
            raise ValueError("Invalid value for `apodsets`, must not be `None`")  # noqa: E501

        self._apodsets = apodsets

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TenantCluster, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TenantCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
