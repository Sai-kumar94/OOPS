class Cube():
    def __init__(self,fv,lv,up=1):
        self.fv=fv
        self.lv=lv
        self.up=up
    def __iter__(self):
        self.i=self.fv
        return self
    def __next__(self):
        if self.i<self.lv:
            d=self.i**3
            self.i+=self.up
            return d
        else:
            raise StopIteration
s=Cube(1,5)
for i in s:
    print(i)


