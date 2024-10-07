from person import *

o_person1 = Person('Joe Schmoe', 90_000)
o_person2 = Person('Jane Smith', 99_000)

print(o_person1.get_salary())

o_person1.set_salary(100_000)
o_person2.set_salary(111_111)

print(o_person1.get_salary())
print(o_person2.get_salary())

