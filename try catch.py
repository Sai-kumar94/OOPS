#example of try with multiple except blocks and ALIASING

print('main started')
l=[11,22,33]
try:
    print('try started')
    ip=int(input('enter index position'))
    print(l[ip])
    print(a)
    print('try ended')
except IndexError as ie:
    print(ie)
except NameError as ne:
    print(ne)
print('main end')
