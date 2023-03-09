# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля)


def print_operation_table(operation, num_rows, num_columns):
    arr=[[operation(i,j) for i in range(1,num_rows+1)] for j in range(1, num_columns+1)]
    for i in arr:
        print(*[f"{x:>3}"for x in i])
line = int(input("Enter the number of lines: "))
columns = int(input("Enter number of columns: "))
print_operation_table(lambda x,y: x*y,line,columns)
