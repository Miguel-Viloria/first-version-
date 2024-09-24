IsTrue= True
balance= 0
name= input("please input your name:")
print("Hello," + name + ", Welcome!")
while IsTrue:
     answer = input("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\nYour choice: ")
     answer= int(answer)
     if answer == 1:
         while IsTrue:
              deposit = float(input("How much are you going to deposit?: "))
              if deposit<=0:
                 print("Invalid")
              else: 
                   balance = balance + deposit 
                   print("New Balance: {balance:.2f}")
                   break
         if answer == 2:
            while IsTrue:
                  withdraw= float(input("How much do you want to withdraw?"))
            if withdraw>balance:
                     print("Invalid")
            else:
                    balance =  balance - withdraw
                    print(f"New balance: {balance:.2f}")
                    break
         elif answer == 3:
               print(f"Balance: {balance:.2f}")
         else:
               print("Exiting")
               Istrue= False 

