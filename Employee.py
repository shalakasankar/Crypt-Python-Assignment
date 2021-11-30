
from Account import Account
import os
clear = lambda: os.system('cls')

class Employee():
    empid_count=1010 
    def __init__(self,name,position,id):
        self.name=name
        self.position=position
        self.id=id
           
    def closeAccount(self,acc,account_array):
        for i in range(len(account_array)):
            if type(account_array[i])==Account:
                if str(account_array[i].accountno)==acc:
                    account_array.pop(i)
                    print("Account successfully closed")  
                
    def displayDetails(self,acc,account_array):
        for i in range(len(account_array)):
            if type(account_array[i])==Account:                                            
              if str(account_array[i].accountno)==acc:
                
                print("Account Number: "+ str(account_array[i].accountno))
                print("Name: "+account_array[i].name)
                print("Account Balance: "+str(account_array[i].balance))
        
                                                                         
    def employeeHomePage(self,account_array):
        ch=1
        while(ch!=4):
            
            print("\n")
            print(self.name)
            print(self.position)
            print("\nView customer details-1")
            if self.id <=1003:
                print("Close account-2")
            if self.id==1000:
                print("Add an employee-3")
            print("Quit-4")
            ch=int(input())

            if ch==1:
                print("Enter account number of customer")
                acc=input()
                self.displayDetails(acc,account_array)

            if ch==2:
                print("Enter account number of customer")
                acc=input()
                self.closeAccount(acc,account_array)
    
            if ch==3:
                print("Enter new Employee name:")
                empname=input()
                print("Enter new Employee post:")
                emppost=input()
                print("Employee I.D Number: "+str(self.empid_count))
                new_employee=Employee(empname,emppost,self.empid_count)
                account_array.append(new_employee)
                self.empid_count+=1
        if ch==4:
            return