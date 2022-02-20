# -*- coding: utf-8 -*-
# @Author: Danilo Diaz Valencia
# @Date:   2022-02-20 11:01:57
# @Last Modified by:   Danilo Diaz Valencia
# @Last Modified time: 2022-02-20 11:52:18
from importlib.resources import path
import re
from unittest import result
from fastapi.testclient import TestClient
from service.main import app
from os import environ
import os
import json

environ['config_file'] = "config.yml"

client = TestClient(app)


def test_value_139():
    response = client.get("/get-nba/139")
    path_result = os.path.join('test', 'json_result', '139.json')
    f = open(path_result)
    result = json.load(f)
    assert response.status_code == 200
    assert response.json() == result

def test_value_100():
    response = client.get("/get-nba/100")
    path_result = os.path.join('test', 'json_result', 'no_result.json')
    f = open(path_result)
    result = json.load(f)
    assert response.status_code == 200
    assert response.json() == result

def test_value_140():
    response = client.get("/get-nba/140")
    path_result = os.path.join('test', 'json_result', '140.json')
    f = open(path_result)
    result = json.load(f)
    assert response.status_code == 200
    assert response.json() == result

def test_value_160():
    response = client.get("/get-nba/160")
    path_result = os.path.join('test', 'json_result', '160.json')
    f = open(path_result)
    result = json.load(f)
    assert response.status_code == 200
    assert response.json() == result