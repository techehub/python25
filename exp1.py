def readnum ():
    num = input ("Enter a number ::")
    return num

def readop ():
    op = input ("Enter a operator ::")
    return op


def main ():
    try :
        x = readnum()
        y = readnum()
        v1 = int(x)
        v2 = int(y)
        op = readop()
        if (op == '+'):
            res = v1 + v2
        elif (op=='/'):
            res = v1 / v2


    except ValueError:
        print ("Invalid number please provide numeric values!!!")
    except ZeroDivisionError:
        print("please don't provide zero")
    except Exception as e:
        print (e)
    else :
        print(res)
    finally:
        print ("inside finally")

while (True):
    main ()





