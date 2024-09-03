
class Address():
    def __init__(self,c,s,cou):
        self.city = c
        self.state=s
        self.country=cou
    def display_address(self):
        print(f'name of the city is {self.city}')
        print(f'name of the state is {self.state}')
        print(f'name of the country is {self.country}')

class Student():
    def __init__(self,sn,sa,sc):
        self.sname=sn
        self.sage=sa
        self.sclass=sc
        c=input('enter city')
        s=input('enter state')
        co=input('enter country')
        ACO=Address(c,s,co)
        self.saddress=ACO
    def student_info(self):
        print(f'name of the student is {self.sname}')
        print(f'age of the student is{self.sage}')
        print(f'class of the student is{self.sclass}')
        print(f'address of the student is')
#       self.saddress=bangaloreobject
        self.saddress.display_address()
deepsika=Student('deepsika',23,'python',)
deepsika.student_info()
shyam=Student('shyam',23,'django')
shyam.student_info()

