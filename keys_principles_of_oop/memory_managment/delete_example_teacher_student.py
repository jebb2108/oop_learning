# класс Student

class Student():
    def __init__(self, name):
        self.name = name
        print('Creating student object for', self.name)

    def __del__(self):
        print('In the __del__ method for student:', self.name)

# Класс Teacher

class Teacher():
    def __init__(self):
        print('Creating the Teacher object')
        self.o_student1 = Student('Joe')
        self.o_student2 = Student('Sue')
        self.o_student3 = Student('Chris')

    def __del__(self):
        print('In the __del__ method for Teacher')

# создаем экземпляр объекта Teacher (и, таким образом, объекты Student)
o_teacher = Teacher()

# Удаляем объект Teacher
del o_teacher
