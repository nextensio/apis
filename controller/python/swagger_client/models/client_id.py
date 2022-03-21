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

class ClientID(object):
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
        'result': 'str',
        'clientid': 'str'
    }

    attribute_map = {
        'result': 'Result',
        'clientid': 'clientid'
    }

    def __init__(self, result=None, clientid=None):  # noqa: E501
        """ClientID - a model defined in Swagger"""  # noqa: E501
        self._result = None
        self._clientid = None
        self.discriminator = None
        self.result = result
        self.clientid = clientid

    @property
    def result(self):
        """Gets the result of this ClientID.  # noqa: E501


        :return: The result of this ClientID.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ClientID.


        :param result: The result of this ClientID.  # noqa: E501
        :type: str
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def clientid(self):
        """Gets the clientid of this ClientID.  # noqa: E501


        :return: The clientid of this ClientID.  # noqa: E501
        :rtype: str
        """
        return self._clientid

    @clientid.setter
    def clientid(self, clientid):
        """Sets the clientid of this ClientID.


        :param clientid: The clientid of this ClientID.  # noqa: E501
        :type: str
        """
        if clientid is None:
            raise ValueError("Invalid value for `clientid`, must not be `None`")  # noqa: E501

        self._clientid = clientid

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
        if issubclass(ClientID, dict):
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
        if not isinstance(other, ClientID):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other