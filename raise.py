print('main started')
try:
    a=int(input())
    b=int(input())
    if b==0:
        raise ZeroDivisionError('WE CANNOT DIVIDE')
except Exception as E:
    print(E)
print('main ended')