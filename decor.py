def outer(arg):#arg=hai function address
    print('outer is started')
    print(arg)
    def inner():
        print('starting of inner function')
        arg()
        print('ending of inner function')
    print('outer is ended')
    return inner
@outer#hai=outer(hai)#hai =inner function address
def hai():
    print('hai starts')
    print('hai ends')
hai()
# result=outer(hai)#inner function address
# print(result)
# result()


def brother(arg):
    def inner():
        print('brother is monitoring')
        arg()
        print('brother is ended monitoring')
    return inner
@brother#sister1=brother(address of sisters1)#sister1=inner function address
def sister1():
    print('sister1 started speaking')
    print('sister1 ended speaking')
sister1()

def sister2():
    print('sister2 started speaking')
    print('sister2 ended speaking')


sister2()









