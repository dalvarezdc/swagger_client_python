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

class CommonConceptLinks(object):
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
        'is_top_concept_in_scheme': 'list[Link]',
        'is_in_scheme': 'list[Link]',
        'broader_concept': 'list[Link]',
        'narrower_concept': 'list[Link]',
        'has_essential_skill': 'list[Link]',
        'has_optional_skill': 'list[Link]'
    }

    attribute_map = {
        'is_top_concept_in_scheme': 'isTopConceptInScheme',
        'is_in_scheme': 'isInScheme',
        'broader_concept': 'broaderConcept',
        'narrower_concept': 'narrowerConcept',
        'has_essential_skill': 'hasEssentialSkill',
        'has_optional_skill': 'hasOptionalSkill'
    }

    def __init__(self, is_top_concept_in_scheme=None, is_in_scheme=None, broader_concept=None, narrower_concept=None, has_essential_skill=None, has_optional_skill=None):  # noqa: E501
        """CommonConceptLinks - a model defined in Swagger"""  # noqa: E501
        self._is_top_concept_in_scheme = None
        self._is_in_scheme = None
        self._broader_concept = None
        self._narrower_concept = None
        self._has_essential_skill = None
        self._has_optional_skill = None
        self.discriminator = None
        if is_top_concept_in_scheme is not None:
            self.is_top_concept_in_scheme = is_top_concept_in_scheme
        if is_in_scheme is not None:
            self.is_in_scheme = is_in_scheme
        if broader_concept is not None:
            self.broader_concept = broader_concept
        if narrower_concept is not None:
            self.narrower_concept = narrower_concept
        if has_essential_skill is not None:
            self.has_essential_skill = has_essential_skill
        if has_optional_skill is not None:
            self.has_optional_skill = has_optional_skill

    @property
    def is_top_concept_in_scheme(self):
        """Gets the is_top_concept_in_scheme of this CommonConceptLinks.  # noqa: E501

        A concept scheme that contains this concept at the top level of its concept hierarchy. The value of this field is an array containing Links to the relevant Taxonomy resources.  # noqa: E501

        :return: The is_top_concept_in_scheme of this CommonConceptLinks.  # noqa: E501
        :rtype: list[Link]
        """
        return self._is_top_concept_in_scheme

    @is_top_concept_in_scheme.setter
    def is_top_concept_in_scheme(self, is_top_concept_in_scheme):
        """Sets the is_top_concept_in_scheme of this CommonConceptLinks.

        A concept scheme that contains this concept at the top level of its concept hierarchy. The value of this field is an array containing Links to the relevant Taxonomy resources.  # noqa: E501

        :param is_top_concept_in_scheme: The is_top_concept_in_scheme of this CommonConceptLinks.  # noqa: E501
        :type: list[Link]
        """

        self._is_top_concept_in_scheme = is_top_concept_in_scheme

    @property
    def is_in_scheme(self):
        """Gets the is_in_scheme of this CommonConceptLinks.  # noqa: E501

        A concept scheme that contains this concept. The value of this field is an array containing Links to the relevant Taxonomy resources.  # noqa: E501

        :return: The is_in_scheme of this CommonConceptLinks.  # noqa: E501
        :rtype: list[Link]
        """
        return self._is_in_scheme

    @is_in_scheme.setter
    def is_in_scheme(self, is_in_scheme):
        """Sets the is_in_scheme of this CommonConceptLinks.

        A concept scheme that contains this concept. The value of this field is an array containing Links to the relevant Taxonomy resources.  # noqa: E501

        :param is_in_scheme: The is_in_scheme of this CommonConceptLinks.  # noqa: E501
        :type: list[Link]
        """

        self._is_in_scheme = is_in_scheme

    @property
    def broader_concept(self):
        """Gets the broader_concept of this CommonConceptLinks.  # noqa: E501

        The value of this field is an array containing Links to broader Concept resources.  # noqa: E501

        :return: The broader_concept of this CommonConceptLinks.  # noqa: E501
        :rtype: list[Link]
        """
        return self._broader_concept

    @broader_concept.setter
    def broader_concept(self, broader_concept):
        """Sets the broader_concept of this CommonConceptLinks.

        The value of this field is an array containing Links to broader Concept resources.  # noqa: E501

        :param broader_concept: The broader_concept of this CommonConceptLinks.  # noqa: E501
        :type: list[Link]
        """

        self._broader_concept = broader_concept

    @property
    def narrower_concept(self):
        """Gets the narrower_concept of this CommonConceptLinks.  # noqa: E501

        The value of this field is an array containing Links to narrower Concept resources.  # noqa: E501

        :return: The narrower_concept of this CommonConceptLinks.  # noqa: E501
        :rtype: list[Link]
        """
        return self._narrower_concept

    @narrower_concept.setter
    def narrower_concept(self, narrower_concept):
        """Sets the narrower_concept of this CommonConceptLinks.

        The value of this field is an array containing Links to narrower Concept resources.  # noqa: E501

        :param narrower_concept: The narrower_concept of this CommonConceptLinks.  # noqa: E501
        :type: list[Link]
        """

        self._narrower_concept = narrower_concept

    @property
    def has_essential_skill(self):
        """Gets the has_essential_skill of this CommonConceptLinks.  # noqa: E501

        An essential skill for this concept. The value of this field is an array containing Links to essential Skill resources.  # noqa: E501

        :return: The has_essential_skill of this CommonConceptLinks.  # noqa: E501
        :rtype: list[Link]
        """
        return self._has_essential_skill

    @has_essential_skill.setter
    def has_essential_skill(self, has_essential_skill):
        """Sets the has_essential_skill of this CommonConceptLinks.

        An essential skill for this concept. The value of this field is an array containing Links to essential Skill resources.  # noqa: E501

        :param has_essential_skill: The has_essential_skill of this CommonConceptLinks.  # noqa: E501
        :type: list[Link]
        """

        self._has_essential_skill = has_essential_skill

    @property
    def has_optional_skill(self):
        """Gets the has_optional_skill of this CommonConceptLinks.  # noqa: E501

        An optional skill for this concept. The value of this field is an array containing Links to essential Skill resources.  # noqa: E501

        :return: The has_optional_skill of this CommonConceptLinks.  # noqa: E501
        :rtype: list[Link]
        """
        return self._has_optional_skill

    @has_optional_skill.setter
    def has_optional_skill(self, has_optional_skill):
        """Sets the has_optional_skill of this CommonConceptLinks.

        An optional skill for this concept. The value of this field is an array containing Links to essential Skill resources.  # noqa: E501

        :param has_optional_skill: The has_optional_skill of this CommonConceptLinks.  # noqa: E501
        :type: list[Link]
        """

        self._has_optional_skill = has_optional_skill

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
        if issubclass(CommonConceptLinks, dict):
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
        if not isinstance(other, CommonConceptLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
