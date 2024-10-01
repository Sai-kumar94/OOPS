def gen_fibo(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b
for num in gen_fibo(10):
    print(num)
#

# normal method:

# def gen_fibo(n):
#     a,b=1,1
#     output=[]
#     for i in range(n):
#         output.append(a)
#         a,b=b,a+b
#     return output
# for num in gen_fibo(10):
#     print(num)
