import re


def parse(elem):
    index = int(elem[1]) - 1
    value = int(elem[0]) if elem[0] else 1
    return (index, value)


def get_param(string, sign):
    x_param, value = string.split(sign)
    result = re.findall(r'(\d+)?x(\d+)', x_param)
    result = list(map(parse, result))
    return result, value

def get_f_parameter(string):
    string = string.replace(' ', '')
    result, criteria = get_param(string, '->')
    count_param = len(result)    
    data = {'func':criteria, 'f_params':[0]*count_param}
    for elem in result:
        index, value = elem
        data['f_params'][index] = value

    return data

def get_sign(string):
    result = re.search(r'([<>]?=)', string)
    return result.group(1)

def get_relation(string):
    string = string.strip()
    string.replace(' ', '')
    sign = get_sign(string)
    x_params, value = get_param(string, sign)
    count = len(x_params)
    data = {'value':value, 'x_params': [0]*count, 'sign': sign}
    for elem in x_params:
        index, key = elem
        data['x_params'][index] = key
    return data


def read_from_file(fh):
    f_string = fh.readline().strip()
    data = get_f_parameter(f_string)
    data['inquat'] = []
    for string in fh:
        data['inquat'].append(get_relation(string))
    return data