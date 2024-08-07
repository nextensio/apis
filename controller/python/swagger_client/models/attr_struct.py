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

class AttrStruct(object):
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
        'name': 'str',
        'applies_to': 'str',
        'type': 'str',
        'is_array': 'str',
        'group': 'str'
    }

    attribute_map = {
        'name': 'name',
        'applies_to': 'appliesTo',
        'type': 'type',
        'is_array': 'isArray',
        'group': 'group'
    }

    def __init__(self, name=None, applies_to=None, type=None, is_array=None, group=None):  # noqa: E501
        """AttrStruct - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._applies_to = None
        self._type = None
        self._is_array = None
        self._group = None
        self.discriminator = None
        self.name = name
        self.applies_to = applies_to
        self.type = type
        self.is_array = is_array
        self.group = group

    @property
    def name(self):
        """Gets the name of this AttrStruct.  # noqa: E501


        :return: The name of this AttrStruct.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AttrStruct.


        :param name: The name of this AttrStruct.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def applies_to(self):
        """Gets the applies_to of this AttrStruct.  # noqa: E501


        :return: The applies_to of this AttrStruct.  # noqa: E501
        :rtype: str
        """
        return self._applies_to

    @applies_to.setter
    def applies_to(self, applies_to):
        """Sets the applies_to of this AttrStruct.


        :param applies_to: The applies_to of this AttrStruct.  # noqa: E501
        :type: str
        """
        if applies_to is None:
            raise ValueError("Invalid value for `applies_to`, must not be `None`")  # noqa: E501

        self._applies_to = applies_to

    @property
    def type(self):
        """Gets the type of this AttrStruct.  # noqa: E501


        :return: The type of this AttrStruct.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AttrStruct.


        :param type: The type of this AttrStruct.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def is_array(self):
        """Gets the is_array of this AttrStruct.  # noqa: E501


        :return: The is_array of this AttrStruct.  # noqa: E501
        :rtype: str
        """
        return self._is_array

    @is_array.setter
    def is_array(self, is_array):
        """Sets the is_array of this AttrStruct.


        :param is_array: The is_array of this AttrStruct.  # noqa: E501
        :type: str
        """
        if is_array is None:
            raise ValueError("Invalid value for `is_array`, must not be `None`")  # noqa: E501

        self._is_array = is_array

    @property
    def group(self):
        """Gets the group of this AttrStruct.  # noqa: E501


        :return: The group of this AttrStruct.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this AttrStruct.


        :param group: The group of this AttrStruct.  # noqa: E501
        :type: str
        """
        if group is None:
            raise ValueError("Invalid value for `group`, must not be `None`")  # noqa: E501

        self._group = group

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
        if issubclass(AttrStruct, dict):
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
        if not isinstance(other, AttrStruct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
