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

class CertStructWithResult(object):
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
        'certid': 'str',
        'cert': 'list[int]'
    }

    attribute_map = {
        'result': 'Result',
        'certid': 'certid',
        'cert': 'cert'
    }

    def __init__(self, result=None, certid=None, cert=None):  # noqa: E501
        """CertStructWithResult - a model defined in Swagger"""  # noqa: E501
        self._result = None
        self._certid = None
        self._cert = None
        self.discriminator = None
        self.result = result
        self.certid = certid
        self.cert = cert

    @property
    def result(self):
        """Gets the result of this CertStructWithResult.  # noqa: E501


        :return: The result of this CertStructWithResult.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this CertStructWithResult.


        :param result: The result of this CertStructWithResult.  # noqa: E501
        :type: str
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def certid(self):
        """Gets the certid of this CertStructWithResult.  # noqa: E501


        :return: The certid of this CertStructWithResult.  # noqa: E501
        :rtype: str
        """
        return self._certid

    @certid.setter
    def certid(self, certid):
        """Sets the certid of this CertStructWithResult.


        :param certid: The certid of this CertStructWithResult.  # noqa: E501
        :type: str
        """
        if certid is None:
            raise ValueError("Invalid value for `certid`, must not be `None`")  # noqa: E501

        self._certid = certid

    @property
    def cert(self):
        """Gets the cert of this CertStructWithResult.  # noqa: E501


        :return: The cert of this CertStructWithResult.  # noqa: E501
        :rtype: list[int]
        """
        return self._cert

    @cert.setter
    def cert(self, cert):
        """Sets the cert of this CertStructWithResult.


        :param cert: The cert of this CertStructWithResult.  # noqa: E501
        :type: list[int]
        """
        if cert is None:
            raise ValueError("Invalid value for `cert`, must not be `None`")  # noqa: E501

        self._cert = cert

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
        if issubclass(CertStructWithResult, dict):
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
        if not isinstance(other, CertStructWithResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
