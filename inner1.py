c= 10000

def calc (a, b) :
    c= 10

    def add ():
        global c
        c=10
        print (a+b +c)

    def sub():
        nonlocal c

        c = 333
        print(a - b -c)

    def mul():
        print(a * b * c)

    add ()
    sub ()
    print (" c after sub", c)
    mul ()


calc (10,10)
print (c)
