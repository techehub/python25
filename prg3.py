
def calc (fff, a,b ):
    return fff (a,b)

def main ():
    num1 = int (input ("Enter num1#"))
    num2 = int (input ("Enter num2#"))
    opr = input ("Enter op::")

    if (opr =="+") :
         aaa= lambda x, y : x+y
         result = calc ( aaa, num1, num2)
         print(" sum of {} and {} is {} ".format(num1, num2, result))
    elif (opr == "-"):
         bbb = lambda x, y: x - y
         result = calc(bbb, num1, num2)
         print(" diff of {} and {} is {} ".format(num1, num2, result))
    else :
         print ("Not supported")

main()