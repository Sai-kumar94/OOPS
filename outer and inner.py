# function called with function address and returning inner function address

def outer(arg):#arg=hai function address
    print('outer is started')
    print(arg)
    def inner():
        print('starting of inner function')
        arg()
        print('ending of inner function')
    print('outer is ended')
    return inner
def hai():
    print('hai starts')
    print('hai ends')

result=outer(hai)#inner function address
print(result)
result()


def outer(arg):
    print('outer function is started')
    print(arg)
    def inner():
        print('inner function  is started')
        print(arg)
        print('ending of inner function')
    print('outer is ending')
    return inner
result=outer(20)
print(result)
result()














