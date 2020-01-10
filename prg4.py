
def sum (a, *num)  :

   print (type(num))
   sum =0
   for i in num:
       sum = sum +i
   return sum +a

def add (a=0, b=10) :
    return a+b

def greet (**v):
    print (type(v))
    print(v)
    print ("Hi", v ['name'], v ['msg'] )

#greet (name="Kumar" , msg="Good morning")
#x = add(10,44)


def test (a, b,  *x,  **y):
    print (x)
    print (y)

test (10, 20, 30, 40, name="Vijeesh")

