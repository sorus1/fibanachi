def fibonacci(n):
    f1 = 0
    f2 = 1
    i = 2

    while (i != n):
        Fn = f1 + f2
        f1 = f2
        f2 = Fn
        i+=1
    print(Fn)




if __name__ == '__main__':
    fibonacci(10)