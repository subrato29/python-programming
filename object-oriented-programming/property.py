class Person:
    def __init__(self, name):
        self.name = name
        self._salary = 0  # private attribute because of using '_', ideally this should not be accessed from outside of class

    @property
    def salary(self):
        return round(self._salary)

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise Exception("Salary is invalid")
        self._salary = salary

    # salary = property (get_salary, set_salary)


p1 = Person("Tom")
p1.salary = 100.11
print(p1.salary)


class Time:
    def __init__(self, second):
        self._second = second

    @property
    def second(self):
        print("running")
        return self._second

    @second.setter
    def second(self, second):
        if second < 0 or second > 60:
            raise Exception("Invalid!")
        self._second = second


t1 = Time(54)
t1.second = 59
print(t1.second)
