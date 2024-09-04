class Satyam:
    house='2BHK'
    bike='pulsar'
    money=100k
manju=Satyam()

class Sai(Satyam):
    bike = 'Kawasaki ninja H2r'
    car='lambo'
wife=Sai()

#accessing parent class properties by using PC,PCO,CC,CCO(parent class,parent class object,child class,child class object)
print(Satyam.money)
print(manju.money)
print(Sai.money)
print(wife.money)

#modifying PC properties by using PC
Satyam.money=1234567
print(Satyam.money)
print(manju.money)
print(Sai.money)
print(wife.money)

#note:
#it modifies in PC,PCO,CC,CCO

# modifying parent class properties by using  PCO

manju.money=987654
print(Satyam.money)
print(manju.money)
print(Sai.money)
print(wife.money)
#note
# it modifies in PCO

#modifying the PCP by using CC

Sai.money=456789
print(Satyam.money)
print(manju.money)
print(Sai.money)
print(wife.money)


#modifying PCP by using CCO

wife.money=87655456
print(Satyam.money)
print(manju.money)
print(Sai.money)
print(wife.money)

#note
#it modifies in CCO





































































