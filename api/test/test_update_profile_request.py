# coding: utf-8

"""
    @ledge/api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ledge_python_sdk.models.update_profile_request import UpdateProfileRequest

class TestUpdateProfileRequest(unittest.TestCase):
    """UpdateProfileRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateProfileRequest:
        """Test UpdateProfileRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateProfileRequest`
        """
        model = UpdateProfileRequest()
        if include_optional:
            return UpdateProfileRequest(
                default = True,
                inventory_id = '',
                product_type = 'GIFT_CARD'
            )
        else:
            return UpdateProfileRequest(
                inventory_id = '',
                product_type = 'GIFT_CARD',
        )
        """

    def testUpdateProfileRequest(self):
        """Test UpdateProfileRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()