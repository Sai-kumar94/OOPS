class Bank():
    bank_name='sbi'
    bank_roi=7
    bank_branch='andhra'
    def __init__(self,n,a,b,cac):
        self.cname=n
        self.cage=a
        self.cbal=b
        self.caccount=cac

    @classmethod
    def bank_details(cls):
        print(f'name of the bank is {cls.bank_name}')
        print(f'bank_roi of the bank is {cls.bank_roi}')
        print(f'branch of the bank is {cls.bank_branch}')

    def customer_details(self):
        print(f'name of the customer is {self.cname}')
        print(f'age of the customer is {self.cage}')
        print(f'balance of the customer is {self.cbal}')
        print(f'account of the customer is {self.caccount}')

    @staticmethod
    def get_int_value():
        iv=int(input('enter value'))
        return iv

    @staticmethod
    def get_str_value():
        sv = input('enter value')
        return sv

    def withdraw(self):
        amount = self.get_int_value()
        if amount <= self.cbal:
            self.cbal -= amount
            print('withdrawal is success full')
            print('balance is ', self.cbal)
        else:
            print('insufficient balance')

    def deposit(self):
        amount = self.get_int_value()
        if amount >0:
            self.cbal += amount
            print(self.cbal)
            print('deposit is done successfully')
        else:
            print('roi is changed')

    @classmethod
    def change_roi(cls):
        newroi = cls.get_int_value()
        cls.bank_roi = newroi
        print('roi is modified')

    @classmethod
    def change_branch(cls):
        bn = cls.get_str_value()
        cls.bank_branch = bn
        print('branch name is changed')


govinda = Bank('govind', 13, 98765, 456789)
malik = Bank('malik ', 14, 5678, 987654)
govinda.withdraw()
malik.deposit()
govinda.bank_details()
govinda.customer_details()









