class Account():
    def __init__(self,name,balance,accountno,id,password,age,dob):
        self.name=name 
        self.balance=balance
        self.accountno=accountno
        self.id=id
        self.password=password
        self.age=age
        self.dob=dob
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance in account")
        else:
            self.balance=self.balance-amount
            print(str(amount)+ "has been withdrawn. Current balance in your account: "+str(self.balance))
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Current balance: "+str(self.balance))
    
    def checkBalance(self):
        return self.balance

    
    def displayHome(self,id):

        print("Account Number: "+str(self.accountno))
        print("Name:"+self.name)
        print("Current Balance: "+str(self.balance))
        print("\n\n")
        ch=0
        while(ch!=4):
            print("1=WITHDRAW \n 2=DEPOSIT \n 3=CHECK BALANCE \n4=QUIT")
            ch=int(input())
            if ch==1:
                print("Enter Amount: ")
                amt=int(input())
                self.withdraw(amt)

            if ch==2:
                print("Enter Amount: ")
                amt=int(input())
                self.deposit(amt)
            
            if ch==3:
                print("Current Balance:" + str(self.checkBalance()))
        
       