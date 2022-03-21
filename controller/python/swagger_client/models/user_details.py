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

class UserDetails(object):
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
        'uid': 'str',
        'name': 'str',
        'email': 'str',
        'gateway': 'str',
        'usertype': 'str',
        'pod': 'int',
        'connectid': 'str',
        'services': 'list[str]'
    }

    attribute_map = {
        'result': 'Result',
        'uid': 'uid',
        'name': 'name',
        'email': 'email',
        'gateway': 'gateway',
        'usertype': 'usertype',
        'pod': 'pod',
        'connectid': 'connectid',
        'services': 'services'
    }

    def __init__(self, result=None, uid=None, name=None, email=None, gateway=None, usertype=None, pod=None, connectid=None, services=None):  # noqa: E501
        """UserDetails - a model defined in Swagger"""  # noqa: E501
        self._result = None
        self._uid = None
        self._name = None
        self._email = None
        self._gateway = None
        self._usertype = None
        self._pod = None
        self._connectid = None
        self._services = None
        self.discriminator = None
        self.result = result
        self.uid = uid
        self.name = name
        self.email = email
        self.gateway = gateway
        self.usertype = usertype
        self.pod = pod
        if connectid is not None:
            self.connectid = connectid
        self.services = services

    @property
    def result(self):
        """Gets the result of this UserDetails.  # noqa: E501


        :return: The result of this UserDetails.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this UserDetails.


        :param result: The result of this UserDetails.  # noqa: E501
        :type: str
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def uid(self):
        """Gets the uid of this UserDetails.  # noqa: E501


        :return: The uid of this UserDetails.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this UserDetails.


        :param uid: The uid of this UserDetails.  # noqa: E501
        :type: str
        """
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

    @property
    def name(self):
        """Gets the name of this UserDetails.  # noqa: E501


        :return: The name of this UserDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserDetails.


        :param name: The name of this UserDetails.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def email(self):
        """Gets the email of this UserDetails.  # noqa: E501


        :return: The email of this UserDetails.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserDetails.


        :param email: The email of this UserDetails.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def gateway(self):
        """Gets the gateway of this UserDetails.  # noqa: E501


        :return: The gateway of this UserDetails.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this UserDetails.


        :param gateway: The gateway of this UserDetails.  # noqa: E501
        :type: str
        """
        if gateway is None:
            raise ValueError("Invalid value for `gateway`, must not be `None`")  # noqa: E501

        self._gateway = gateway

    @property
    def usertype(self):
        """Gets the usertype of this UserDetails.  # noqa: E501


        :return: The usertype of this UserDetails.  # noqa: E501
        :rtype: str
        """
        return self._usertype

    @usertype.setter
    def usertype(self, usertype):
        """Sets the usertype of this UserDetails.


        :param usertype: The usertype of this UserDetails.  # noqa: E501
        :type: str
        """
        if usertype is None:
            raise ValueError("Invalid value for `usertype`, must not be `None`")  # noqa: E501

        self._usertype = usertype

    @property
    def pod(self):
        """Gets the pod of this UserDetails.  # noqa: E501


        :return: The pod of this UserDetails.  # noqa: E501
        :rtype: int
        """
        return self._pod

    @pod.setter
    def pod(self, pod):
        """Sets the pod of this UserDetails.


        :param pod: The pod of this UserDetails.  # noqa: E501
        :type: int
        """
        if pod is None:
            raise ValueError("Invalid value for `pod`, must not be `None`")  # noqa: E501

        self._pod = pod

    @property
    def connectid(self):
        """Gets the connectid of this UserDetails.  # noqa: E501


        :return: The connectid of this UserDetails.  # noqa: E501
        :rtype: str
        """
        return self._connectid

    @connectid.setter
    def connectid(self, connectid):
        """Sets the connectid of this UserDetails.


        :param connectid: The connectid of this UserDetails.  # noqa: E501
        :type: str
        """

        self._connectid = connectid

    @property
    def services(self):
        """Gets the services of this UserDetails.  # noqa: E501


        :return: The services of this UserDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this UserDetails.


        :param services: The services of this UserDetails.  # noqa: E501
        :type: list[str]
        """
        if services is None:
            raise ValueError("Invalid value for `services`, must not be `None`")  # noqa: E501

        self._services = services

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
        if issubclass(UserDetails, dict):
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
        if not isinstance(other, UserDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
