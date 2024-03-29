import re


def parse(elem):
    index = int(elem[2]) - 1
    value = float(elem[1]) if elem[1] else 1
    if elem[0] == '-':
        value *= -1
    return (index, value)


def get_param(string, sign):
    string = string.replace(' ', '')
    x_param, value = string.split(sign)
    result = re.findall(r'([-+])?([0-9.]+)?x(\d+)', x_param)
    result = list(map(parse, result))
    return result, value

def get_f_parameter(string):
    result, criteria = get_param(string, '->')
    count_param = len(result)    
    data = {'func':criteria, 'f_params':[0]*count_param}
    for elem in result:
        index, value = elem
        data['f_params'][index] = value
    data['count'] = len(data['f_params'])
    return data

def get_sign(string):
    result = re.search(r'([<>]?=)', string)
    return result.group(1)

def get_relation(string, count):
    string = string.strip()
    string.replace(' ', '')
    sign = get_sign(string)
    x_params, value = get_param(string, sign)
    data = {'value':int(value), 'x_params': [0]*count, 'sign': sign}
    for elem in x_params:
        index, key = elem
        data['x_params'][index] = key
    return data


def read_from_file(filename):
    """
    Read input from file
    Returns:
    dict:
    {
        f_params: [],
        inquat: [
            {
                value: int,
                x_params: [],
                sign: string
            }
        ],

    }
    """
    with open(filename, 'r') as fh:
        f_string = fh.readline().strip()
        data = get_f_parameter(f_string)
        data['inquat'] = []
        for string in fh:
            data['inquat'].append(get_relation(string, data['count']))
    return data