def singleton(arg): #arg=multiplex CA
    L=[]
def inner():
    if not L:
        MCO=arg()
        L.append(MCO)
        return L[0]
    return inner

@singleton # multiplex=singleton(multiplex CA) #multiplex =inner function address

class Multiplex:
    def __init__(self):
        self.tickets=300
    def booking(self,nt):
        if nt<=self.tickets:
            print('booking is successfull')
            print('remaining tickets are ',self.tickets)
        else:
            print('tickets not available')
            print('remaining tickets are ',self.tickets)
nara=Multiplex()
nara.booking(200)
print(nara)
hari=Multiplex()
hari.booking(150)
print(hari)
pru=Multiplex()
pru.booking(1)
print(pru)

