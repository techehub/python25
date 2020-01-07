
def calc():
    pass

def calcinterest(p,r, n):
    res= p *r *n/100
    return res


def main():
    p = eval(input("Amount ::"))
    r = eval(input("Rate ::"))
    n = eval(input("Term :"))

    logic = calcinterest
    x1 = logic (p,r,n)
    print (logic)
    print(x1)


main()