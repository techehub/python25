def test (a, b):
    print("a",id(a))
    print("b",id(b))
    a=a+10
    print("a", id(a))



def main ():
    x = 10
    y = 20
    print ("x",id (x))
    print("y",id(y))
    test(x,y)
    print (x)

main ()