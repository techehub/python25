class Shape:
   def area(self):
       return None


class Rectangle (Shape):

   def __init__(self,w,h):
       self.width=w
       self.height =h

   def area (self):
       return self.width *  self.height

   def display(self):
       print ("Rectangle")


class Circle (Shape) :

   def __init__(self, r):
       self.radius = r

   def area (self):
       return 3.14 * self.radius* self.radius

   def display(self):
       print ("Circle")


def displayArea( x):
   print ("-------------")
   print (x.__class__)
   print (x.area())
   x.display()


def main ():

   shape1= Circle(30)
   shape2= Rectangle(10,20)
   shape3 = Circle(20)

   displayArea(shape1)
   displayArea(shape2)
   displayArea(shape3)


main()
