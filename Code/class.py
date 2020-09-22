class Student:
    def __init__(self, student_id, first_name, last_name):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.grades = {}
    
    def add_grade(self, course, grade):
        self.grades[course] = grade
    
    def get_gpa(self):
        sum_ = 0
        for g in self.grades.values():
            sum_ += g
        return sum_ / len(self.grades) 
    
    def __repr__(self):
        return "{} {}, {}".format(self.first_name, self.last_name, self.student_id)

    def __lt__(self):
        return "{} {}, {}".format(self.first_name, self.last_name, self.student_id)

jiawei = Student("6519409", "Jiawei", "Li")

print("{} {}, {}".format(jiawei.first_name, jiawei.last_name, jiawei.student_id))
print(jiawei)
