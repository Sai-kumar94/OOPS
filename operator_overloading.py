class Book:
    def __init__(self,n,au,p):
        self.bname=n
        self.bauthor=au
        self.bprice=p
    def __str__(self):
        return self.bname
    def __add__(self, second):
        #self=pythonobject
        #second=django object
        return self.bprice+second.bprice
    def __sub__(self, second):
        return self.bprice-second.bprice

    def __mul__(self,value):
        return self.bprice*value

    def __truediv__(self, value):
        return self.bprice/value
python=Book('python','GVR',1234)
django=Book('django','sk',76543)
print(python+django)
print(python-django)
print(python*3)
print(python/2)
















