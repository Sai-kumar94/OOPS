def genfunction():
    print('genf is started ')
    yield 25
    print('content of genf after first yield')
    yield 'hello'
    print('content of genf after second yield')
    print('last')
    yield 89,74,'bye'
gnf=genfunction()
print(gnf)
print(next(gnf))
print(next(gnf))
print(next(gnf))
print(next(gnf))
