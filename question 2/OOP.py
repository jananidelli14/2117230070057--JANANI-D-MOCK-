class Student:
    def __init__(self,name,marks):
         self.name=name
         self.marks=marks
    def getGrade(self):
         if self.marks>=90:
              return 'A'
         elif self.marks>=80:
              return 'B'
         else:
              return 'C'
s=Student("janani",98)
print(s.getGrade())
         

