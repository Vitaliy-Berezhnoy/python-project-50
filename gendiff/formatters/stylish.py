import json

OFFSET = 4
SPACE = ' '
SYMBOL = {'add': '+ ', 'del': '- ', 'match': '  ', 'nested': '  '}


def convert_value(value, depth, OFFSET, SPACE):
    if isinstance(value, dict):
        depth += 1
        temp = ['{\n']
        for key in value:
            val = convert_value(value[key], depth, OFFSET, SPACE)
            temp.extend([f'{SPACE * OFFSET * depth}{key}: ', *val, '\n'])
        depth -= 1
        temp.append(f'{SPACE * OFFSET * depth}{'}'}')
        return temp            
    if not isinstance(value, str):
        return json.dumps(value)
    return value


def make_format_stylish(diff: dict, OFFSET, SPACE, SYMBOL) -> str:

    def make_line(t_diff: dict, key, depth):        
        offset = SPACE * (OFFSET * depth - len(SYMBOL['add']))
        if t_diff[key]['status'] == 'mod':
            val1 = convert_value(t_diff[key]['val'], depth, OFFSET, SPACE)
            val2 = convert_value(t_diff[key]['val2'], depth, OFFSET, SPACE)
            return [f'{offset}{SYMBOL['del']}{key}: ', *val1, '\n',
                    f'{offset}{SYMBOL['add']}{key}: ', *val2, '\n']
        if t_diff[key]['status'] == 'nested':
            temp_list = [f'{offset}{SYMBOL['nested']}{key}: {'{\n'}']
            val = t_diff[key]['val']
            for child in val:
                temp_list.extend(make_line(val, child, depth + 1))
            temp_list.append(f'{SPACE * OFFSET * depth}{'}\n'}')
            return temp_list              
        symbol = SYMBOL[t_diff[key]['status']]         
        val = convert_value(t_diff[key]['val'], depth, OFFSET, SPACE)
        return [f'{offset}{symbol}{key}: ', *val, '\n']
    
    result = ['{\n']
    for child in diff:
        result.extend(make_line(diff, child, 1))
    result.append('}')
    return ''.join(result)
