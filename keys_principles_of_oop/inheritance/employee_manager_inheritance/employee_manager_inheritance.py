# Наследование Employee Manager
#
# Определяем класс Employee, который мы будем использовать как
# базовый классс

class Employee:
    def __init__(self, name, title, rate_per_hour=None):
        self.name = name
        self.title = title
        if rate_per_hour is not None:
            rate_per_hour = float(rate_per_hour)
        self.rate_per_hour = rate_per_hour

    def get_name(self):
        return self.name

    def get_title(self):
        return self.title

    def pay_per_year(self):
        # 52 недели * 5 дней в неделю * 8 часов в день
        pay = 52 * 5 * 8 * self.rate_per_hour
        return pay

# Определяем класс Manager, который наследует от Employee

class Manager(Employee):
    def __init__(self, name, title, salary, reports_list=None):
        self.salary = float(salary)
        if reports_list is None:
            self.reports_list = []
        self.reports_list = reports_list
        super().__init__(name, title)

    def get_reports(self):
        return self.reports_list

    def pay_per_year(self, give_bonus=False):
        pay = self.salary
        if give_bonus:
            pay = pay + (.10 * self.salary)  # добавляем бонус 10%
            print(self.name, 'gets a bonus for good work')
        return pay

# создаем объекты
o_employee1 = Employee('Joe Schmoe', 'Pizza Maker', 16)
o_employee2 = Employee('Chris Smith', 'Cashier', 14)
o_manager = Manager('Sue Jones', 'Pizza Restaurant Manager',  55000, [o_employee1, o_employee2])

# вызываем методы объектов Employee
print('Employee name:', o_employee1.get_name())
print('Employee salary:', '{:,.2f}'.format(o_employee1.pay_per_year()))
print('Employee name:', o_employee2.get_name())
print('Employee salary:', '{:,.2f}'.format(o_employee2.pay_per_year()))
print()

# вызываем методы объектов Manager
print('Manager name:', o_manager.get_name())

# Даем менеджеру бонус
print('Manager salary:', '{:,.2f}'.format(o_manager.pay_per_year(True)))
print(o_manager.get_name(), '(' + o_manager.get_title() + ') gets a bonus for good work')
report_list = o_manager.get_reports()
for o_employee in report_list:
    print(' ', o_employee.get_name(),
          '(', o_employee.get_title(), ')')
