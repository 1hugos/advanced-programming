def list_of_num (num):
    new_list = []
    for x in num:
        new_list.append(x * 2)

    return new_list

def list_of_num_2 (num):
    new_list = [x*2 for x in num]

    return new_list

numbers = [1,2,3,4,5]

print('Podejście i:')

new_numbers = list_of_num(numbers)

for x in new_numbers:
    print(x)

print('Podejście ii:')

new_numbers_2 = list_of_num_2(numbers)

for x in new_numbers_2:
    print(x)