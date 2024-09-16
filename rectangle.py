class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def __gt__(self, other):
        area1=self.length*self.breadth
        area2=other.length*other.breadth
        return True if area1>area2 else False
R1=Rectangle(12,34)
R2=Rectangle(12,43)
print(R1>R2)



# second type

class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
        self.area=l*b
    def __gt__(self, other):
       if self.area>other.area:
           return True
       else:
           return False

R1=Rectangle(12,34)
R2=Rectangle(12,43)
print(R1>R2)