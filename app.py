class Student:
    def __init__(self, name, school):
        self.name = name
        self.school =school
        self.marks = [55,36]
    
    def average(self):
        return sum(self.marks)/len(self.marks)
    
    def __str__(self):
        return 'Name: %s, School: %s' %(self.name, self.school)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name,school)
        self.salary = salary
    
    def weekly_salary(self):
        return self.salary * 30
    def __str__(self):
        return super().__str__()+ ", " + "Salary: "+str(self.weekly_salary())


s1 = Student('just-student', 'MIT')
s1.marks = [98, 63, 87, 98]
print("just-student average marks: ",s1.average())
print(s1)
s2 = WorkingStudent('working-student', 'JKU', 20)
print(s2)