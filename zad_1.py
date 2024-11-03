class Student:
    def __init__(self, name, marks):
        self._name = name
        self._marks = marks
 
    def is_passed (self) -> bool:
        average = (sum(self._marks) / len(self._marks))

        return average > 50
        
student_1 = Student('Mark', [90, 60, 30, 20, 40, 70])
student_2 = Student('Emily', [10, 20, 20, 30, 40, 20])

print(student_1.is_passed())
print(student_2.is_passed())
 