# Написать функцию, возвращающую четные элементы последовательности Фибоначчи
# Пример: f4 вернет последовательность 0, 2, 8, 34

def show_even_fibonacci(n):
    a = 0
    b = 1
    if n < 1:
        return
    print(0, end=' ')
    n -= 1
    while(n > 0):
        c = a + b
        if c & 1 == 0:
           print(c, end=' ' )
           n -= 1
        a = b
        b = c



if  __name__ == '__main__':
    show_even_fibonacci(4)