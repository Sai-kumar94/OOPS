def d_error(arg):
    def inner(a,b):#a=10,b=2 #a=10,b=0
        if b==0:
            arg(b,a) #division(10,0)
        else:
            arg(a,b) #division(10,0)
    return inner
@d_error
def division(a,b):
    print(a/b)
division(10,2)
division(10,0)