def only_second_item(num):
    for i in range(len(num)):
        if i % 2 == 0:
            print(num[i])
