def is_even(number: int) -> bool:

    if number % 2 == 0:
        return True
    else:
        return False


answer = is_even(23)

if answer is True:
    print('Liczba jest parzysta')
else:
    print('Liczba jest nieparzysta')
