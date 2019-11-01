
from Controller import algorithm
from Controller import make_table
from Controller import prog_input

from pprint import pprint

if __name__ == '__main__':
    data = prog_input.read_from_file('tests/input_test.txt')
    pprint(data)

    table = make_table.create_table(data)
    for i in table:
        print(*i)

    q = 0
    while not algorithm.check_f_params(table):
        r_row, r_col = algorithm.find_resolve_elements(table)
        print("Разрешающая строка", r_row)
        print("разрешающий столбец", r_col)
        table = algorithm.calculate_new_table(table, r_row, r_col)
        q += 1

        for i in table:
            print(*i)

    print('RESULT')
    for i in table:
        print(*i)
