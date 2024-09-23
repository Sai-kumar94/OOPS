# demonstration of range function by using generator
def rangeGen(LL,UL,UP=1):
    while LL<UL:
        yield LL
        LL+=UP
rgo=rangeGen(1,10,2)
for i in rgo:
    print(i)


def genFibo(fv,sv,n):
    i=1
    while i<n+1:
        yield fv
        fv,sv=sv,fv+sv
        i+=1
gfo=genFibo(2,3,9)
for i in gfo:
    print(i)



#size of memory for generator and iterator

def gen():
    i=1
    while i<2:
        yield i
        i+=1
go=gen()
print(go.__sizeof__())
print(iter([11]).__sizeof__())




