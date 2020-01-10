class Student (object) :

    def __init__ (self, name, rollno, branch, m1, m2, m3):
        self.name = name
        self.__rollno = rollno
        self._branch = branch
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
        print("Rollno :", self.__rollno)
        print("Branch :", self._branch)
        print("Total :", self.total())
        print("Average :", self.avg())


class FulltimeStudent (Student ):

    def __init__(self, name, rollno, branch, m1, m2, m3, hours):
        super().__init__(name, rollno, branch, m1, m2, m3)
        self.hours = hours

    def display (self):
        super().display()
        print ("Hour :", self.hours)
        print("Rollno :", self._branch)


s1 = FulltimeStudent("Kabeer", "123", "CS", 22, 33, 44, 5)
s2 = FulltimeStudent("Seetha", "222", "CS", 25, 35, 45, 6)
s3 = FulltimeStudent("Tom", "333", "CS", 26, 36, 46, 7)

print (s1.__dict__)
s1._Student__rollno= "QQQQQQQ"


s1.display()
s2.display()
s3.display()


x = getattr(s1, "_Student__rollno")
print (x)
setattr(s1, "name", "Peter")
print (hasattr(s1, "subject"))
print (s1.name)

delattr(s1, "_branch")
print (hasattr(s1, "_branch"))
print (s1.__dict__)



