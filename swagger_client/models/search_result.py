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
from swagger_client.models.suggestion_result import SuggestionResult  # noqa: F401,E501

class SearchResult(SuggestionResult):
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
        'facets': 'dict(str, dict(str, int))'
    }
    if hasattr(SuggestionResult, "swagger_types"):
        swagger_types.update(SuggestionResult.swagger_types)

    attribute_map = {
        'facets': 'facets'
    }
    if hasattr(SuggestionResult, "attribute_map"):
        attribute_map.update(SuggestionResult.attribute_map)

    def __init__(self, facets=None, *args, **kwargs):  # noqa: E501
        """SearchResult - a model defined in Swagger"""  # noqa: E501
        self._facets = None
        self.discriminator = None
        if facets is not None:
            self.facets = facets
        SuggestionResult.__init__(self, *args, **kwargs)

    @property
    def facets(self):
        """Gets the facets of this SearchResult.  # noqa: E501

        Per facet the different values and the number of occurrences (count) in the result set.  # noqa: E501

        :return: The facets of this SearchResult.  # noqa: E501
        :rtype: dict(str, dict(str, int))
        """
        return self._facets

    @facets.setter
    def facets(self, facets):
        """Sets the facets of this SearchResult.

        Per facet the different values and the number of occurrences (count) in the result set.  # noqa: E501

        :param facets: The facets of this SearchResult.  # noqa: E501
        :type: dict(str, dict(str, int))
        """

        self._facets = facets

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
        if issubclass(SearchResult, dict):
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
        if not isinstance(other, SearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
