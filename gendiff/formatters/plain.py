import json


def get_values(value) -> str:
    if isinstance(value, dict):
        return '[complex value]'
    return json.dumps(value).replace('"', "'")


def make_line(path: str, values: dict) -> list:
    val = get_values(values['val'])
    if values['status'] == 'match':
        return []
    if values['status'] == 'del':
        tail = 'removed'
    elif values['status'] == 'add':
        tail = f"added with value: {val}"
    elif values['status'] == 'mod':
        tail = f'updated. From {val} to {get_values(values['val2'])}'
    return [f"Property '{path}' was {tail}"]


def processing_key(key: str, values: dict, path='') -> list:
    t_path = path + key
    result = []
    if values['status'] != 'nested':
        line = make_line(t_path, values)
        return line
    for child in values['val']:
        result.extend(processing_key(child, values['val'][child], t_path + '.'))
    return result


def make_format_plain(diff: dict) -> str:
    out_result = []
    for key in diff:
        out_result.extend(processing_key(key, diff[key], ''))
    return '\n'.join(out_result)
