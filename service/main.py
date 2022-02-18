# -*- coding: utf-8 -*-
# @Author: Danilo Diaz Valencia
# @Date:   2022-02-18 16:32:35
# @Last Modified by:   Danilo Diaz Valencia
# @Last Modified time: 2022-02-18 17:38:25
import sys
import os
import typing as t
from datetime import datetime
from functools import lru_cache
from modelling import app as logic
from service.schema import ResultNBAPair

from fastapi import FastAPI, Depends, Body, Path  # type: ignore # noqa: E402
from pydantic import BaseSettings, PositiveFloat


app = FastAPI(
    title="API to make NBA Player Pair based of heights", version="0.0.1")


class Settings(BaseSettings):
    config_file: str


@lru_cache(None)
def get_settings():
    return Settings()


@lru_cache(None)
def load_data():
    sys.path.append(get_settings().config_file)
    data = logic._get_dataset(logic._load_config(
        get_settings().config_file, "data"))
    return data


@app.get("/get-nba/{value}")
async def nba_pairs(
        value: int = Path(...),
        data=Depends(load_data)):
    
    row = logic.DataInValues(data)
    row.findpairs(value = value)
    result = row.get_pairs()
    return result
