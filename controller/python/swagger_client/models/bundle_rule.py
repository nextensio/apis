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

class BundleRule(object):
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
        'bid': 'str',
        'rid': 'str',
        'group': 'str',
        'rule': 'list[list[str]]'
    }

    attribute_map = {
        'bid': 'bid',
        'rid': 'rid',
        'group': 'group',
        'rule': 'rule'
    }

    def __init__(self, bid=None, rid=None, group=None, rule=None):  # noqa: E501
        """BundleRule - a model defined in Swagger"""  # noqa: E501
        self._bid = None
        self._rid = None
        self._group = None
        self._rule = None
        self.discriminator = None
        self.bid = bid
        self.rid = rid
        self.group = group
        self.rule = rule

    @property
    def bid(self):
        """Gets the bid of this BundleRule.  # noqa: E501


        :return: The bid of this BundleRule.  # noqa: E501
        :rtype: str
        """
        return self._bid

    @bid.setter
    def bid(self, bid):
        """Sets the bid of this BundleRule.


        :param bid: The bid of this BundleRule.  # noqa: E501
        :type: str
        """
        if bid is None:
            raise ValueError("Invalid value for `bid`, must not be `None`")  # noqa: E501

        self._bid = bid

    @property
    def rid(self):
        """Gets the rid of this BundleRule.  # noqa: E501


        :return: The rid of this BundleRule.  # noqa: E501
        :rtype: str
        """
        return self._rid

    @rid.setter
    def rid(self, rid):
        """Sets the rid of this BundleRule.


        :param rid: The rid of this BundleRule.  # noqa: E501
        :type: str
        """
        if rid is None:
            raise ValueError("Invalid value for `rid`, must not be `None`")  # noqa: E501

        self._rid = rid

    @property
    def group(self):
        """Gets the group of this BundleRule.  # noqa: E501


        :return: The group of this BundleRule.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this BundleRule.


        :param group: The group of this BundleRule.  # noqa: E501
        :type: str
        """
        if group is None:
            raise ValueError("Invalid value for `group`, must not be `None`")  # noqa: E501

        self._group = group

    @property
    def rule(self):
        """Gets the rule of this BundleRule.  # noqa: E501


        :return: The rule of this BundleRule.  # noqa: E501
        :rtype: list[list[str]]
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this BundleRule.


        :param rule: The rule of this BundleRule.  # noqa: E501
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
        if issubclass(BundleRule, dict):
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
        if not isinstance(other, BundleRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other