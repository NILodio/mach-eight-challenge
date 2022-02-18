# -*- coding: utf-8 -*-
# @Author: Danilo Diaz Valencia
# @Date:   2022-02-18 17:20:34
# @Last Modified by:   Danilo Diaz Valencia
# @Last Modified time: 2022-02-18 17:33:50
import typing as t
from pydantic import root_validator
import typing_extensions as te

from pydantic import BaseModel, Field, ConstrainedInt, PositiveInt, PositiveFloat


class PlayerNBA(BaseModel):
    full_name : t.Optional[str]
    first_name : str
    h_in: str
    h_meters: str
    last_name: str

    @root_validator
    def compute_name(cls, values):
        values['full_name'] = values.get("first_name") + values.get("last_name")
        return values

    

class DetailsResult(BaseModel):
    NBA_Pair_1 : t.List[PlayerNBA]
    NBA_Pair_2 : t.List[PlayerNBA]


class ResultNBAPair(BaseModel):
    result: t.List[DetailsResult]
