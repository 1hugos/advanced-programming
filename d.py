def only_second_item (num):
    for i in range(len(num)):
        if i % 2 == 0:
            print(num[i])

numbers = list(range(10))

only_second_item(numbers)