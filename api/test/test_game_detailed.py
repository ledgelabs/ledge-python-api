# coding: utf-8

"""
    @ledge/api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ledge_python_sdk.models.game_detailed import GameDetailed

class TestGameDetailed(unittest.TestCase):
    """GameDetailed unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameDetailed:
        """Test GameDetailed
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameDetailed`
        """
        model = GameDetailed()
        if include_optional:
            return GameDetailed(
                play_store_id = '',
                app_store_id = '',
                logo_url = '',
                banner_url = '',
                banner_title = '',
                icon_url = '',
                description = '',
                title = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                game_tags = [
                    null
                    ],
                game_genres = [
                    null
                    ]
            )
        else:
            return GameDetailed(
                play_store_id = '',
                app_store_id = '',
                logo_url = '',
                banner_url = '',
                banner_title = '',
                icon_url = '',
                description = '',
                title = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                game_tags = [
                    null
                    ],
                game_genres = [
                    null
                    ],
        )
        """

    def testGameDetailed(self):
        """Test GameDetailed"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
