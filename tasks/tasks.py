import tasks.zad_1.a as zad_1_a 
import tasks.zad_1.b as zad_1_b 
import tasks.zad_1.c as zad_1_c 
import tasks.zad_1.d as zad_1_d


def run_tasks():
    #zad 1a
    print('Zadanie 1a:')
    list_of_names = ['Jeff', 'John', 'Mark', 'Joey', 'Andrew']

    zad_1_a.display_names(list_of_names)

    #zad 1b
    print('Zadanie 1b:')
    numbers = [1, 2, 3, 4, 5]

    print('Podejście i:')

    new_numbers = zad_1_b.list_of_num(numbers)

    for x in new_numbers:
        print(x)

    print('Podejście ii:')

    new_numbers_2 = zad_1_b.list_of_num_2(numbers)

    for x in new_numbers_2:
        print(x)

    #zad 1c
    print('Zadanie 1c:')

    numbers = list(range(10))

    zad_1_c.only_odd(numbers)

    #zad 1d
    print('Zadanie 1d:')

    numbers = list(range(10))

    zad_1_d.only_second_item(numbers)