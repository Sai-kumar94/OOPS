class Fib():
    def __init__(self,a,b,n):
        self.fv=a
        self.sv=b
        self.num=n
    def __iter__(self):
        self.ll=1
        return self
    def __next__(self):
        if self.ll<=self.num:
            self.ll += 1
            dum=self.fv
            self.fv=self.sv
            self.sv=dum+self.fv
            return dum
        else:
            raise StopIteration
k=Fib(1,2,7)
for i in k:
    print(i)
