# coding: utf-8

"""
    @ledge/api

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
from ledge_python_sdk.models.product import Product
from typing import Optional, Set
from typing_extensions import Self

class DrawProductDetailed(BaseModel):
    """
    DrawProductDetailed
    """ # noqa: E501
    product_id: StrictStr = Field(alias="productId")
    draw_id: StrictStr = Field(alias="drawId")
    qty: Union[StrictFloat, StrictInt]
    updated_at: datetime = Field(alias="updatedAt")
    created_at: datetime = Field(alias="createdAt")
    id: StrictStr
    product: Optional[Product]
    __properties: ClassVar[List[str]] = ["productId", "drawId", "qty", "updatedAt", "createdAt", "id", "product"]

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
        """Create an instance of DrawProductDetailed from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of product
        if self.product:
            _dict['product'] = self.product.to_dict()
        # set to None if product (nullable) is None
        # and model_fields_set contains the field
        if self.product is None and "product" in self.model_fields_set:
            _dict['product'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DrawProductDetailed from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "productId": obj.get("productId"),
            "drawId": obj.get("drawId"),
            "qty": obj.get("qty"),
            "updatedAt": obj.get("updatedAt"),
            "createdAt": obj.get("createdAt"),
            "id": obj.get("id"),
            "product": Product.from_dict(obj["product"]) if obj.get("product") is not None else None
        })
        return _obj


