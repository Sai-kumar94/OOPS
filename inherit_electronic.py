class ElectronicDevice():
    def __init__(self,b,m,p):
        self.brand=b
        self.model=m
        self.price=p
    def turn_on(self):
        print(f'{self.brand} {self.model} is turned on')

    def turn_off(self):
        print(f'{self.brand} {self.model} is turned off')
    def get_product_details(self):
        print(f'{self.brand} price is {self.price} and the model is {self.model}')

class Laptop(ElectronicDevice):
    def __init__(self,b,m,p,pro,rom,ram):
        super().__init__(b,m,p)
        # super().get_product_details()
        self.processor=pro
        self.rom=rom
        self.ram=ram

    def run_program(self):
        print(f'{self.brand} {self.model} is running a program ')

class Mouse(ElectronicDevice):
    def __init__(self,b,m,p,c,rbut,lbut):
        super().__init__(b,m,p)
        super().get_product_details()
        # ElectronicDevice.get_product_details(self)
        self.colour=c
        self.right_button=rbut
        self.left_button = lbut

    def onclick(self):
        print(f'{self.right_button} is clicked')
lap=Laptop("apple", "M1",138000,"M1",512,16)
mouse=Mouse("logitech","t1",10000,"black","right button","left button")
lap.turn_on()
lap.run_program()
lap.get_product_details()
print(lap.processor)#price is an instance attribute, not a method. To access it we would use lap.processor.
print(lap.price)#price is an instance attribute, not a method. To access it we would use lap.price.




