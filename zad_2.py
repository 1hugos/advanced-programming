from datetime import date

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library in {self.city}, {self.street}, {self.zip_code}, Open: {self.open_hours}, Phone: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}, Hired: {self.hire_date}, Born: {self.birth_date}, Contact: {self.phone}"


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}, Marks: {self.marks}"

    def is_passed(self):
        return sum(self.marks) / len(self.marks) > 50


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: '{self.author_name} {self.author_surname}', Published: {self.publication_date}, Pages: {self.number_of_pages}, Available at: {self.library}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n  ".join(str(book) for book in self.books)
        return f"Order Date: {self.order_date}\nProcessed by: {self.employee}\nStudent: {self.student}\nBooks:\n  {books_str}"

library1 = Library("New York", "New 1", "00-001", "9:00 - 17:00", "123-456-789")
library2 = Library("Paris", "Old 2", "00-002", "07:00 - 15:00", "987-654-321")

employee1 = Employee("John", "Oak", date(2022, 1, 10), date(1985, 5, 20), "Warsaw", "Long 1", "00-003", "111-222-333")
employee2 = Employee("Ana", "Schwarz", date(2021, 2, 11), date(1990, 4, 21), "Berlin", "Short 2", "00-004", "444-555-666")
employee3 = Employee("Peter", "Parkour", date(2020, 3, 12), date(1995, 6, 22), "Milano", "Curved 3", "00-005", "777-888-999")

book1 = Book(library1, date(2010, 4, 15), "Mark", "Twain", 400)
book2 = Book(library1, date(1998, 9, 1), "Jane", "Austen", 500)
book3 = Book(library2, date(2005, 7, 18), "Charles", "Dickens", 350)
book4 = Book(library2, date(2015, 11, 5), "Mary", "Shelley", 450)
book5 = Book(library1, date(2020, 1, 25), "Ernest", "Hemingway", 300)

order1 = Order(employee1, "Greg", [book1, book3], date(2023, 11, 1))
order2 = Order(employee2, "Sebastian", [book2, book4, book5], date(2023, 11, 2))


print(order1)
print("\n")
print(order2)
