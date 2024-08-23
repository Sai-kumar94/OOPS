class Bank:
    bank_name='sbi'
    bank_ifsc=1234
    bank_address='andhra'
    def __init__(self,cn,cac,cb):
        self.cname=cn
        self.account=cac
        self.bal=cb
    def customer_details(self):
        print(f'name of the customer is {self.cname}')
        print(f'account of the customer is {self.account}')
        print(f'balance of the customer is {self.bal}')
    def withdrawal(self):
        amount=int(input('enter amount : '))
        if self.bal>=amount:
            self.bal-=amount
            print('amount withdrawal successfull')
            print(f'balance is {self.bal}')
        else:
            print('insufficient balance')
    def deposite(self):
        amount=int(input('enter amount : '))
        if amount>0:
            self.bal+=amount
            print("deposite is successfull")
        else:
            print('enter the amount more than 1')

thaneesh=Bank('thaneesh',456767,10000)
sai=Bank('sai',87654,20000)
#thaneesh.customer_details()
#Bank.customer_details('sai')

thaneesh.withdrawal()
thaneesh.deposite()
