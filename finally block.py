#aliasing
print('main start')
l=[11,22,33]
try:
    print('try started')
    n1=int(input())
    n2=int(input())
    res=n1/n2
    print('try ended')
except Exception as E:
    print(E)
else:
    print('inside else block')
    print(res)
finally:
    print('finally is getting executed')
print('main ended')

