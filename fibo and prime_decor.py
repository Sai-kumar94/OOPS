import time
def time_decor(arg):#arg=fib FA
    def inner():
        IT= time.time()
        arg()
        FI= time.time()
        print(FI-IT)
    return inner
@time_decor #fib=time_decor(fib FA)#fib=inner FA
def fib():
    fn=int(input())
    sn = int(input())
    n = int(input())
    if n==1:
        print(fn)
    elif n==2:
        print(fn,sn)
    else:
        print(fn,sn)
        for i in range(n-2):
            tn=fn+sn
            print(tn)
            fn,sn=sn,tn
fib()

@time_decor
def prime_number():
    LL=int(input())
    UL=int(input())
    for n in range(LL,UL+1):
        if n>1:
            for i in range(2,n//2+1):
                if n%i==0:
                    break
            else:
                print(n)
prime_number()