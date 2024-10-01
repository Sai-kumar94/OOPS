print('main start')
try:
    print('try is started ')
    print(a)
    try:
        print('inner try is started')
        print(10/2)
        print('inner try is ended')
    except Exception as E:
        print(E)
    print('outer try is ended')
except Exception as E:
    print(E)
print('main ended')