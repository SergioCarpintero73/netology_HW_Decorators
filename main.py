from foo_logs import logger
from foo_logs import path_to_logs


#Задача №1
@logger
def summa(*args):
    return sum(args)

#Задача №2
@path_to_logs(r'C:\Users\Администратор\PycharmProjects\Decorators')
def multiply(a, b):
    return a * b


if __name__ == '__main__':
    # print(summa(5, 6))
    print(multiply(5, 6))