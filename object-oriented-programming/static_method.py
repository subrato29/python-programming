class Student:
    grade_bump = 2.0

    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades

    # instance method
    def average(self):
        return sum(self.grades) / len(self.grades)

    # static method should not access class attribute
    @staticmethod
    def get_average(grades):
        return sum(grades) / len(grades)

    # class method has the access to the attribute to the class amd static method
    @classmethod
    def get_average_plus_bump(cls, grades):
        average = cls.get_average(grades)
        return min(average + cls.grade_bump, 100)


s1 = Student("Tim", [80, 40, 50, 60])
s2 = Student("David", [10, 20, 30, 40])

average1 = s1.get_average(s1.grades)
average2 = s2.get_average(s2.grades)
print(average1, average2)
