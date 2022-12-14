# coding: utf-8

"""
    ESCO REST API Docs

    The ESCO REST API exposes ESCO as a simple, RESTful API.<br /><br /> <a href=\"esco-api-openapi-v3.yml\">Open API v3 definition</a>  # noqa: E501

    OpenAPI spec version: 1.0.12
    Contact: EMPL-ESCO-SECRETARIAT@ec.europa.eu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.bulk_operation_api import BulkOperationApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBulkOperationApi(unittest.TestCase):
    """BulkOperationApi unit test stubs"""

    def setUp(self):
        self.api = BulkOperationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_concept_by_concept_scheme(self):
        """Test case for get_concept_by_concept_scheme

        Get concepts - by Concept Scheme  # noqa: E501
        """
        pass

    def test_get_concept_by_uri(self):
        """Test case for get_concept_by_uri

        Get concepts - by URIs  # noqa: E501
        """
        pass

    def test_get_occupation_by_concept_scheme(self):
        """Test case for get_occupation_by_concept_scheme

        Get occupations - by Concept Scheme  # noqa: E501
        """
        pass

    def test_get_occupation_by_uri(self):
        """Test case for get_occupation_by_uri

        Get occupations - by URIs  # noqa: E501
        """
        pass

    def test_get_skill_by_concept_scheme(self):
        """Test case for get_skill_by_concept_scheme

        Get skills - by Concept Scheme  # noqa: E501
        """
        pass

    def test_get_skill_by_uri(self):
        """Test case for get_skill_by_uri

        Get skills - by URIs  # noqa: E501
        """
        pass

    def test_get_taxonomy_by_uri(self):
        """Test case for get_taxonomy_by_uri

        Get concept schemes - by URIs  # noqa: E501
        """
        pass

    def test_resource_related_get(self):
        """Test case for resource_related_get

        Get related resources  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
