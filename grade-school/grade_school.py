from collections import OrderedDict


class School(object):
    def __init__(self):
        self.students = dict()

    def add_student(self, name, grade):
        self.students[name] = grade
        self.students = OrderedDict(sorted(self.students.items(), key=lambda x: (x[1], x[0])))

    def roster(self):
        return list(self.students.keys())

    def grade(self, grade_number):
        return [name for name, grade in self.students.items() if grade == grade_number]
