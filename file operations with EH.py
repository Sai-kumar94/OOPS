print('main started')
try:
    FO=open('hello.txt','x')
    try:
        data=eval(input('enter data'))
        FO.write(data)
    except Exception as E:
        print(E)
    finally:
        FO.close()
        print(FO.closed)
except Exception as E:
    print(E)
print('Main ended')