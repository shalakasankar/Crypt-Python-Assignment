from Account import Account
from Employee import Employee
import os
clear = lambda: os.system('cls')
class Main():
   id_count=2000
   empid_count=1010 
   account_array= list()

   e1=Employee("Susan Bones","Manager",1000)
   e2=Employee("Phillip Dunphy","Assistant Manager",1001)
   e3=Employee("Jay Prichett","Finance Managaer",1002)
   account_array.append(e1)
   account_array.append(e2)
   account_array.append(e3)
   ch=0
   while(ch!=3):
    clear()
    print("Existing user? To Log-in press 1")
    print("New user? To create a bank account press 2")
    print("To Exit press 3")
    ch=int(input())
   
    if ch==1:
        clear()
        print("Enter id")
        Id=int(input())  
        length=len(account_array)                 
        for i in range(0,len(account_array)):
            if account_array[i].id==Id:
                if Id < (2000):
                    account_array[i].employeeHomePage(account_array)
                    break
                else:
                    print("Enter Account Number:")
                    acc=input()
                    print("Enter password:")
                    password=input()
                    while( password!=account_array[i].password or acc!=str(account_array[i].accountno)):
                        print("Incorrect Password/Account no.Please try again")
                        print("Enter Account Number:")
                        acc=input()
                        print("Enter password:")
                        password=input()
                    clear()
                    account_array[i].displayHome(Id)


    if ch==2:
        clear()
        print("I.D: "+ str(id_count))
        
        print("Enter Name: ")
        name=input()
        print("Enter your age")
        age=int(input())
        print("Enter Date of birth(DD/MM/YY")
        dob=input()
        print("Enter your password")
        password=input()
        print("Confirm your password")
        password_confirm=input()
        while( password!=password_confirm):
            print("Please check your password again")
            password_confirm=input()
            
        print("\nGenerating account number...")
        Accountno=5051387790000+id_count
        clear()
        a=Account(name,0,Accountno,id_count,password,age,dob)
        account_array.append(a)
        
        a.displayHome(id_count)
        id_count+=1
