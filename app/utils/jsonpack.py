from flask import json

#### json  数据定义


def json_pack(dict):
    json_packed = json.dumps(dict)
    return json_packed