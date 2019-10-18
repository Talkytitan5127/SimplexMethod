from fractions import Fraction

import prog_input


def remove_odds(data):
    for elem in data['inquat']:
        if elem['sign'] == '<=':
            elem['x_params'].append(1)
        elif elem['sign'] == '>=':
            elem['x_params'].append(-1)
    return data


def change_sings(data):
    if data['func'] == 'max':
        data['func'] = 'min'
        data['f_params'] = list(map(lambda x: x*(-1), data['f_params']))
    
    data['f_params'] = list(map(lambda x: x*(-1), data['f_params']))

    for elem in data['inquat']:
        x_params = elem['x_params']
        if x_params[-1] < 0:
            elem['value'] *= -1
            for index in range(len(x_params) - 1):
                x_params[index] *= -1

    return data


def create_table(data):
    table = []
    for elem in data['inquat']:
        table.append(
            [elem['value']] + elem['x_params'][:-1]
        )
    table.append([0] + data['f_params'])
    return table
