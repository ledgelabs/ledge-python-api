# coding: utf-8

"""
    @ledge/api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ledge_python_sdk.models.get_profile200_response import GetProfile200Response

class TestGetProfile200Response(unittest.TestCase):
    """GetProfile200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetProfile200Response:
        """Test GetProfile200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetProfile200Response`
        """
        model = GetProfile200Response()
        if include_optional:
            return GetProfile200Response(
                id = '',
                provider = 'discord',
                nickname = '',
                email = '',
                owner = ledge_python_sdk.models.user_connection.UserConnection(
                    user_id = '', 
                    social_id = '', 
                    social_connection_type = 'discord', 
                    nickname = '', 
                    email = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '', )
            )
        else:
            return GetProfile200Response(
                id = '',
                provider = 'discord',
                nickname = '',
                email = '',
                owner = ledge_python_sdk.models.user_connection.UserConnection(
                    user_id = '', 
                    social_id = '', 
                    social_connection_type = 'discord', 
                    nickname = '', 
                    email = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '', ),
        )
        """

    def testGetProfile200Response(self):
        """Test GetProfile200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()