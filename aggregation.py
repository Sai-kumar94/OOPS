
class Address:
    def __init__(self,area,city,state):
        self.area=area
        self.city=city
        self.state=state

    def display_address(self):
        print('area is ',self.area)
        print('city is ',self.city)
        print('state is',self.state)

class Student():
    def __init__(self,name,a,cl,addr):
        self.name=name
        self.age=a
        self. Class=cl
        self.addr=addr

    def display_student_info(self):
        print('student name ',self.name)
        print('student age ', self.age)
        print('student class ', self.Class)
        print('student address ',end='')
        self.addr.display_address()

bangaloreobj = Address('oar',"BANGALORE",'karnataka')

s1=Student('sai',10,2,bangaloreobj)
#student sai is pointing to the bangalore object
s1.display_student_info()




# example 2


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
    def __init__(self,sn,sa,sc,sad):
        self.sname=sn
        self.sage=sa
        self.sclass=sc
        self.saddress=sad
    def student_info(self):
        print(f'name of the student is  {self.sname}')
        print(f'name of the sage is  {self.sage}')
        print(f'name of the class is  {self.sclass}')
        print(f'name of the address is')

        self.saddress.display_address()
address=Address('bangalore','karnataka','india')
mache=Student('mache',23,'halo',address)
mache.student_info()




# example:3


class Car:
    def __init__(self,n,mn,c):
        self.cname=n
        self.cmodel=mn
        self.ccolour=c
    def start(self):
        print(f'{self.cname} is started')
    def accelerated(self):
        print(f'{self.cname} is accelerated')
    def stop(self):
        print(f'{self.cname} is stopped')
class Driver:
    def __init__(self,n,id,a):
        self.dname =n
        self.did=id
        self.age=a
        na=input("enter carname")
        mnr=input("enter modelnumber")
        cc=input("enter car colour")
        #     creating a car object
        carobject=Car(na,mnr,cc)
        self.Dcar=carobject
    def driving(self):
        print('car is started')
        self.Dcar.start()
        self.Dcar.accelerated()
        self.Dcar.stop()
        print('car is stopped')
D1=Driver('somesh',1234,23)
D1.driving()

# example 4

class Player:
    def __init__(self,n,a,cou,mat,wic,r):
        self.pname=n
        self.page=a
        self.pcountry=cou
        self.pmatches=mat
        self.pwickets=wic
        self.pruns=r
class Team:
    def __init__(self,n):
        self.nop=n
        self.pl=[]
        for i in range(self.nop):
            n=input('enter pname')
            a=int(input('enter page'))
            cou=input('enter p_country')
            mat=int(input('enter matches played'))
            wic=int(input('enter number of wickets taken'))
            runs=int(input('enter runs'))
            player_object=Player(n,a,cou,mat,wic,runs)
            self.pl.append(player_object)

    def max_wicket_taker(self):
        most_wicket_taker_object=self.pl[0] # assume that initial wickets =0
        for po in self.pl:
            if po.pwickets>most_wicket_taker_object.pwickets:
                most_wicket_taker_object=po
            return most_wicket_taker_object.pname


    def max_run_scorer(self):
        max_run_scorer_object=self.pl[0] # assume that initial runs =0
        for po in self.pl:
            if po.pruns>max_run_scorer_object.pruns:
                max_run_scorer_object=po
            return max_run_scorer_object.pname
india=Team(3)
print(india.max_wicket_taker())
print(india.max_run_scorer())


















































