plants = {
    "V": "Violets",
    "R": "Radishes",
    "C": "Clover",
    "G": "Grass"
}


class Garden(object):
    def __init__(self, diagram, students=None):
        if students is None:
            students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet",
                        "Ileana", "Joseph", "Kincaid", "Larry"]
        else:
            students.sort()

        self.diagram = diagram.splitlines()
        self.students = students
        
    def plants(self, student):
        student_index = self.students.index(student) * 2

        result = [
            plants[self.diagram[0][student_index]],
            plants[self.diagram[0][student_index + 1]],
            plants[self.diagram[1][student_index]],
            plants[self.diagram[1][student_index + 1]]
        ]

        return result
