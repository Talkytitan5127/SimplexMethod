

def check_f_params(table):
    row = table[-1]
    for index in range(len(row)):
        if row[index] > 0:
            return False
    else:
        return True


def check_s_params(table):
    column = 0
    for index in range(len(table)-1):
        if table[index][column] < 0:
            return index
    else:
        return -1

def find_resolve_string(table, column=0):
    if not column:
        for index in range(len(table)):
            if table[index][column] < 0:
                return index
    else:
        min_index = -1
        min_value = 10**5
        for index in range(1, len(table)):
            relative = table[index][0] / table[index][column]
            if relative > 0 and relative < min_value:
                min_index = index
                min_value = relative
        return min_index


def find_resolve_column(table, row):
    for index in range(1, len(table[0])):
        if row != -1 and table[row][index] < 0:
            return index
        elif row == -1 and table[row][index] > 0:
            return index
    else:
        return 0


def calculate_new_table(table, r_row, r_column):
    n = len(table)
    m = len(table[0])
    result = [[0]*m for i in range(n)]

    result[r_row][r_column] = 1 / table[r_row][r_column]

    for row in range(n):
        for column in range(m):
            if row == r_row and column != r_column:
                result[row][column] = table[row][column] / table[r_row][r_column]
            elif column == r_column and row != r_row:
                result[row][column] = -1 * table[row][column] / table[r_row][r_column]
            elif column != r_column and row != r_row:
                result[row][column] = table[row][column] - ((table[row][r_column] * table[r_row][column]) / table[r_row][r_column])

    return result                


def find_resolve_elements(table):
    check_s = check_s_params(table)
    if check_s != -1:
        r_col = find_resolve_column(table, check_s)
        r_row = find_resolve_string(table, check_s)
    else:
        r_col = find_resolve_column(table, check_s)
        r_row = find_resolve_string(table, r_col)
    
    return (r_row, r_col)

def simplex_method(table):
    while not check_f_params(table):
        r_row, r_col = find_resolve_elements(table)
        table = calculate_new_table(table, r_row, r_col)
        yield table

if __name__ == '__main__':
    num_iteration = 0
    table = [
        [2, 1, -2],
        [-2, -2, 1],
        [5, 1, 1],
        [0, 1, -1]
    ]
    print("Исходная таблица")
    for i in table:
        print(*i)
    new_table = table
    q = 0
    while not check_f_params(new_table):
        print("iteration", q)
        print("check f", check_f_params(new_table))
        
        r_row, r_col = find_resolve_elements(new_table)

        print("разрешающая строка,", r_row)
        print("разрешающий столбец", r_col)

        new_table = calculate_new_table(new_table, r_row, r_col)
        print("новая матрица")
        for i in new_table:
            print(*i)
        q += 1
        

