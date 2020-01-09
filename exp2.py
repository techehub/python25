class InvalidAmountError (Exception) :
   pass

class InvalidAccountError (Exception):
   pass

class InSufficientFundError (Exception):
   pass

acc_data = { "123": 22222, "222": 21323.66 }


def withdraw(accno, amt):
   if amt > 10000:
       raise InvalidAmountError()
   if accno not in acc_data :
       raise InvalidAccountError()
   if acc_data[accno] < amt :
       raise InSufficientFundError()

   acc_data[accno] = acc_data[accno] - amt


def main ():

   while True:
       print ("#######################################")
       try :
           acc_no = input ("Enter acc number")
           amount = input ("Enter amount")
           withdraw(acc_no, int(amount))
       except InvalidAccountError as e:
           print (e)
           print ("Account is invalid")

       except InSufficientFundError as e:
           print (e)
           print ("Insuffient fund error")

       except InvalidAmountError as  e:
           print (e)
           print ("Invalid amout error")

       except :
           print ("Somthing wrong !!!")



main ()
