# coding: utf-8

"""
    @ledge/external-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from ledge_python_sdk.models.gender import Gender
from typing import Optional, Set
from typing_extensions import Self

class User(BaseModel):
    """
    Model User
    """ # noqa: E501
    last_login: Optional[datetime] = Field(alias="lastLogin")
    verified: StrictBool
    merged_with: Optional[StrictStr] = Field(alias="mergedWith")
    game_id: Optional[StrictStr] = Field(alias="gameId")
    external_id: Optional[StrictStr] = Field(alias="externalId")
    referred_by_id: Optional[StrictStr] = Field(alias="referredById")
    enable_notifications: StrictBool = Field(alias="enableNotifications")
    has_accepted_legal: StrictBool = Field(alias="hasAcceptedLegal")
    has_onboarded: StrictBool = Field(alias="hasOnboarded")
    gender: Gender
    birth_year: Union[StrictFloat, StrictInt] = Field(alias="birthYear")
    avatar: StrictStr
    remaining_referrals: Union[StrictFloat, StrictInt] = Field(alias="remainingReferrals")
    code: StrictStr
    usertag: Union[StrictFloat, StrictInt]
    username: StrictStr
    name: StrictStr
    phone_number: Optional[StrictStr] = Field(alias="phoneNumber")
    email: Optional[StrictStr]
    updated_at: datetime = Field(alias="updatedAt")
    created_at: datetime = Field(alias="createdAt")
    id: StrictStr
    __properties: ClassVar[List[str]] = ["lastLogin", "verified", "mergedWith", "gameId", "externalId", "referredById", "enableNotifications", "hasAcceptedLegal", "hasOnboarded", "gender", "birthYear", "avatar", "remainingReferrals", "code", "usertag", "username", "name", "phoneNumber", "email", "updatedAt", "createdAt", "id"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of User from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if last_login (nullable) is None
        # and model_fields_set contains the field
        if self.last_login is None and "last_login" in self.model_fields_set:
            _dict['lastLogin'] = None

        # set to None if merged_with (nullable) is None
        # and model_fields_set contains the field
        if self.merged_with is None and "merged_with" in self.model_fields_set:
            _dict['mergedWith'] = None

        # set to None if game_id (nullable) is None
        # and model_fields_set contains the field
        if self.game_id is None and "game_id" in self.model_fields_set:
            _dict['gameId'] = None

        # set to None if external_id (nullable) is None
        # and model_fields_set contains the field
        if self.external_id is None and "external_id" in self.model_fields_set:
            _dict['externalId'] = None

        # set to None if referred_by_id (nullable) is None
        # and model_fields_set contains the field
        if self.referred_by_id is None and "referred_by_id" in self.model_fields_set:
            _dict['referredById'] = None

        # set to None if phone_number (nullable) is None
        # and model_fields_set contains the field
        if self.phone_number is None and "phone_number" in self.model_fields_set:
            _dict['phoneNumber'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "lastLogin": obj.get("lastLogin"),
            "verified": obj.get("verified"),
            "mergedWith": obj.get("mergedWith"),
            "gameId": obj.get("gameId"),
            "externalId": obj.get("externalId"),
            "referredById": obj.get("referredById"),
            "enableNotifications": obj.get("enableNotifications"),
            "hasAcceptedLegal": obj.get("hasAcceptedLegal"),
            "hasOnboarded": obj.get("hasOnboarded"),
            "gender": obj.get("gender"),
            "birthYear": obj.get("birthYear"),
            "avatar": obj.get("avatar"),
            "remainingReferrals": obj.get("remainingReferrals"),
            "code": obj.get("code"),
            "usertag": obj.get("usertag"),
            "username": obj.get("username"),
            "name": obj.get("name"),
            "phoneNumber": obj.get("phoneNumber"),
            "email": obj.get("email"),
            "updatedAt": obj.get("updatedAt"),
            "createdAt": obj.get("createdAt"),
            "id": obj.get("id")
        })
        return _obj

