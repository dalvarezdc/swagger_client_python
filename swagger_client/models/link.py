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

class Link(object):
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
        'uri': 'str',
        'href': 'str',
        'title': 'str',
        'code': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'href': 'href',
        'title': 'title',
        'code': 'code'
    }

    def __init__(self, uri=None, href=None, title=None, code=None):  # noqa: E501
        """Link - a model defined in Swagger"""  # noqa: E501
        self._uri = None
        self._href = None
        self._title = None
        self._code = None
        self.discriminator = None
        self.uri = uri
        self.href = href
        self.title = title
        if code is not None:
            self.code = code

    @property
    def uri(self):
        """Gets the uri of this Link.  # noqa: E501

        The uri of the related resource. It is the unique and persistent identifier of the related resource.  # noqa: E501

        :return: The uri of this Link.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this Link.

        The uri of the related resource. It is the unique and persistent identifier of the related resource.  # noqa: E501

        :param uri: The uri of this Link.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def href(self):
        """Gets the href of this Link.  # noqa: E501

        The hyperlink to navigate to the related resource.  # noqa: E501

        :return: The href of this Link.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Link.

        The hyperlink to navigate to the related resource.  # noqa: E501

        :param href: The href of this Link.  # noqa: E501
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def title(self):
        """Gets the title of this Link.  # noqa: E501

        The default label of the related resource. This property provides a human-readable identifier in the negotiated language.  # noqa: E501

        :return: The title of this Link.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Link.

        The default label of the related resource. This property provides a human-readable identifier in the negotiated language.  # noqa: E501

        :param title: The title of this Link.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def code(self):
        """Gets the code of this Link.  # noqa: E501

        An optional code of the related resource.  # noqa: E501

        :return: The code of this Link.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Link.

        An optional code of the related resource.  # noqa: E501

        :param code: The code of this Link.  # noqa: E501
        :type: str
        """

        self._code = code

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
        if issubclass(Link, dict):
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
        if not isinstance(other, Link):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
