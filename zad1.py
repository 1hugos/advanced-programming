def full_name(name: str, surname: str) -> str:
    return f'Cześć {name} {surname}!'


name = 'Mark'
surname = 'Oak'

full_name = full_name(name=name, surname=surname)

print(full_name)
