# -*- coding: utf-8 -*-
# @Author: Danilo Diaz Valencia
# @Date:   2022-02-18 11:02:34
# @Last Modified by:   Danilo Diaz Valencia
# @Last Modified time: 2022-02-18 16:49:21
import json
import os
import shutil
import typing as t
from datetime import datetime, timezone
from functools import lru_cache
from wsgiref.simple_server import demo_app
import requests
from modelling import data

import yaml
import typer

app = typer.Typer()


@lru_cache(None)
def _read_url(url):
    r = requests.get(url)
    return r.json()


class JsonDatasetReader:
    def __init__(self, url: str):
        self.url = url

    def __call__(self):
        return _read_url(self.url)


class DataInValues:
    def __init__(self, data: list):
        self.data = data
        self.result = []

    def findpairs(self, value: int):
        self.hashmap = {}
        self.count = 0
        for i in range(0, len(self.data)):
            self.temp = []
            v = int(self.data[i]['h_in'])
            t = value - v
            if (t in self.hashmap):
                self.count += 1
                self.result.append({f'NBA_Pair_{self.count}': [
                                   self.data[i], self.data[self.hashmap[t]]]})
            self.hashmap[int(self.data[i]['h_in'])] = i

    def get_pairs(self):
        if len(self.result) >= 2:
            return {'result': self.result}
        else:
            return {'result': "No matches found"}


@app.command()
def model(config_file: str, value: int , save_version : bool):
    data = _get_dataset(_load_config(config_file, "data"))
    object_value = DataInValues(data)
    object_value.findpairs(value=value)
    output_dir = _load_config(config_file, "export")["output_dir"]
    result = object_value.get_pairs()
    if save_version:
        version = _save_version(result, output_dir)
        return version
    else:
        return result

def _get_dataset(data_config):
    url = data_config["url"]
    reader = JsonDatasetReader(url)
    return data.get_dataset(reader=reader)


def _save_version(hyperparams: t.Dict[str, t.List[t.List]], output_dir: str):
    version = str(datetime.now(timezone.utc).replace(second=0, microsecond=0))
    version = version.replace(':', ' ')
    model_dir = os.path.join(output_dir, version)
    os.makedirs(model_dir, exist_ok=True)
    try:
        _save_json(hyperparams, os.path.join(model_dir, "params.json"))
    except Exception as e:
        typer.echo(f"Coudln't serialize model due to error {e}")
        shutil.rmtree(model_dir)
    return version


@app.command()
def test(config_file: str):
    print("Hola")
    return "Hola"


def _load_config(filepath: str, key: str):
    content = _load_yaml(filepath)
    config = content[key]
    return config


@lru_cache(None)
def _load_yaml(filepath: str) -> t.Dict[str, t.Any]:
    with open(filepath, "r") as f:
        content = yaml.safe_load(f)
    return content


def _save_json(content, filepath: str):
    with open(filepath, "w") as f:
        json.dump(content, f, indent=4)


if __name__ == "__main__":
    app()
