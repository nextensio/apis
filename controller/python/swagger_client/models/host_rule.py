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

class HostRule(object):
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
        'host': 'str',
        'rid': 'str',
        'group': 'str',
        'rule': 'list[list[str]]'
    }

    attribute_map = {
        'host': 'host',
        'rid': 'rid',
        'group': 'group',
        'rule': 'rule'
    }

    def __init__(self, host=None, rid=None, group=None, rule=None):  # noqa: E501
        """HostRule - a model defined in Swagger"""  # noqa: E501
        self._host = None
        self._rid = None
        self._group = None
        self._rule = None
        self.discriminator = None
        self.host = host
        self.rid = rid
        self.group = group
        self.rule = rule

    @property
    def host(self):
        """Gets the host of this HostRule.  # noqa: E501


        :return: The host of this HostRule.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this HostRule.


        :param host: The host of this HostRule.  # noqa: E501
        :type: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def rid(self):
        """Gets the rid of this HostRule.  # noqa: E501


        :return: The rid of this HostRule.  # noqa: E501
        :rtype: str
        """
        return self._rid

    @rid.setter
    def rid(self, rid):
        """Sets the rid of this HostRule.


        :param rid: The rid of this HostRule.  # noqa: E501
        :type: str
        """
        if rid is None:
            raise ValueError("Invalid value for `rid`, must not be `None`")  # noqa: E501

        self._rid = rid

    @property
    def group(self):
        """Gets the group of this HostRule.  # noqa: E501


        :return: The group of this HostRule.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this HostRule.


        :param group: The group of this HostRule.  # noqa: E501
        :type: str
        """
        if group is None:
            raise ValueError("Invalid value for `group`, must not be `None`")  # noqa: E501

        self._group = group

    @property
    def rule(self):
        """Gets the rule of this HostRule.  # noqa: E501


        :return: The rule of this HostRule.  # noqa: E501
        :rtype: list[list[str]]
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this HostRule.


        :param rule: The rule of this HostRule.  # noqa: E501
        :type: list[list[str]]
        """
        if rule is None:
            raise ValueError("Invalid value for `rule`, must not be `None`")  # noqa: E501

        self._rule = rule

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
        if issubclass(HostRule, dict):
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
        if not isinstance(other, HostRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
