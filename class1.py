class Student :

    def __init__ (self, name, rollno, branch, m1, m2, m3):
        self.name = name
        self.rollno = rollno
        self.branch = branch
        self.mark1 = m1
        self.mark2 = m2
        self.mark3 = m3


    def total (self):
        return self.mark1 + self.mark2 + self.mark3

    def avg (self):
        return self.total()/3


    def display (self):
        print ("--------------------")
        print ("Name :", self.name)
        print("Rollno :", self.rollno)
        print("Branch :", self.branch)
        print("Total :", self.total())
        print("Average :", self.avg())



s1 = Student("Kabeer", "123", "CS", 22, 33, 44)
s2 = Student("Seetha", "222", "CS", 25, 35, 45)
s3 = Student("Tom", "333", "CS", 26, 36, 46)

s1.display()
s2.display()
s3.display()

