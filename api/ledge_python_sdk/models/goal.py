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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from ledge_python_sdk.models.activity_type import ActivityType
from typing import Optional, Set
from typing_extensions import Self

class Goal(BaseModel):
    """
    Model Goal
    """ # noqa: E501
    object_id: Optional[StrictStr] = Field(alias="objectId")
    quest_id: StrictStr = Field(alias="questId")
    activity: ActivityType
    banner_url: Optional[StrictStr] = Field(alias="bannerUrl")
    target: Union[StrictFloat, StrictInt]
    instructions: Optional[StrictStr]
    description: StrictStr
    title: StrictStr
    updated_at: datetime = Field(alias="updatedAt")
    created_at: datetime = Field(alias="createdAt")
    id: StrictStr
    __properties: ClassVar[List[str]] = ["objectId", "questId", "activity", "bannerUrl", "target", "instructions", "description", "title", "updatedAt", "createdAt", "id"]

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
        """Create an instance of Goal from a JSON string"""
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
        # set to None if object_id (nullable) is None
        # and model_fields_set contains the field
        if self.object_id is None and "object_id" in self.model_fields_set:
            _dict['objectId'] = None

        # set to None if banner_url (nullable) is None
        # and model_fields_set contains the field
        if self.banner_url is None and "banner_url" in self.model_fields_set:
            _dict['bannerUrl'] = None

        # set to None if instructions (nullable) is None
        # and model_fields_set contains the field
        if self.instructions is None and "instructions" in self.model_fields_set:
            _dict['instructions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Goal from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "objectId": obj.get("objectId"),
            "questId": obj.get("questId"),
            "activity": obj.get("activity"),
            "bannerUrl": obj.get("bannerUrl"),
            "target": obj.get("target"),
            "instructions": obj.get("instructions"),
            "description": obj.get("description"),
            "title": obj.get("title"),
            "updatedAt": obj.get("updatedAt"),
            "createdAt": obj.get("createdAt"),
            "id": obj.get("id")
        })
        return _obj


