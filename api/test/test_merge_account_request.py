# coding: utf-8

"""
    @ledge/api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ledge_python_sdk.models.merge_account_request import MergeAccountRequest

class TestMergeAccountRequest(unittest.TestCase):
    """MergeAccountRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MergeAccountRequest:
        """Test MergeAccountRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MergeAccountRequest`
        """
        model = MergeAccountRequest()
        if include_optional:
            return MergeAccountRequest(
                internal_user_id = ''
            )
        else:
            return MergeAccountRequest(
        )
        """

    def testMergeAccountRequest(self):
        """Test MergeAccountRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
