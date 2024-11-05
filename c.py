def only_odd(num):
    for x in num:
        if x % 2 == 0:
            print(x)


numbers = list(range(10))

only_odd(numbers)
