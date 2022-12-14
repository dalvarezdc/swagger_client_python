# coding: utf-8

"""
    ESCO REST API Docs

    The ESCO REST API exposes ESCO as a simple, RESTful API.<br /><br /> <a href=\"esco-api-openapi-v3.yml\">Open API v3 definition</a>  # noqa: E501

    OpenAPI spec version: 1.0.12
    Contact: EMPL-ESCO-SECRETARIAT@ec.europa.eu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Code(object):
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
        'datatype': 'str',
        'value': 'str'
    }

    attribute_map = {
        'datatype': 'datatype',
        'value': 'value'
    }

    def __init__(self, datatype=None, value=None):  # noqa: E501
        """Code - a model defined in Swagger"""  # noqa: E501
        self._datatype = None
        self._value = None
        self.discriminator = None
        if datatype is not None:
            self.datatype = datatype
        self.value = value

    @property
    def datatype(self):
        """Gets the datatype of this Code.  # noqa: E501

        The datatype of the code literal. Used to identify the code type or the code list to which the code belongs to.  # noqa: E501

        :return: The datatype of this Code.  # noqa: E501
        :rtype: str
        """
        return self._datatype

    @datatype.setter
    def datatype(self, datatype):
        """Sets the datatype of this Code.

        The datatype of the code literal. Used to identify the code type or the code list to which the code belongs to.  # noqa: E501

        :param datatype: The datatype of this Code.  # noqa: E501
        :type: str
        """

        self._datatype = datatype

    @property
    def value(self):
        """Gets the value of this Code.  # noqa: E501

        The code literal. The value of this field is a string.  # noqa: E501

        :return: The value of this Code.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Code.

        The code literal. The value of this field is a string.  # noqa: E501

        :param value: The value of this Code.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(Code, dict):
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
        if not isinstance(other, Code):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
