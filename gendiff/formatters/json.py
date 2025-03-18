import json


def make_format_json(diff: dict):
    return json.dumps(diff, indent=2)
