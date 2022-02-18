# -*- coding: utf-8 -*-
# @Author: Danilo Diaz Valencia
# @Date:   2022-02-18 11:27:14
# @Last Modified by:   Danilo Diaz Valencia
# @Last Modified time: 2022-02-18 11:46:17
import typing as t
import typing_extensions as te
from datetime import date ,datetime
from random import randint


class DataserReader(te.Protocol):
    def __call__(self) -> dict:
        ...

def get_dataset(reader):
    data = reader()
    return data['values']
