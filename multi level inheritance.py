class A:
    a=10
    def __init__(self):
        print('__init__ of A class')
class B(A):
    b=20
    def __init__(self):
        print('__init__ of B class')
class C(B):
    pass
OB=B()#B class constructor will be called
OC=C()#B class constructor will be called
print(C.mro()) #[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
               #C-------->B--------->A--------->OBJECT










