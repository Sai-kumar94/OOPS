d={i:i**3 for i in range(1,5)}
print(d)

T=11,22,33,44
d={i:i**2 for i in T}
print(d)

str='aBc'
d={i.upper():(i*3).lower() for i in str}
print(d)


str='aBc'
d={str[ip].upper():str[ip].lower()*(ip+1) for ip in range(len(str)) }
print(d)

#
str='aBc'
d={ip:str[ip] for ip in range(len(str)) }
print(d)


str='aBc'
print(list(enumerate(str)))
d={key:value for key,value in enumerate(str)}
print(d)

L=[10,20,30]
S='abc'
d={S[ip]:L[ip] for ip in range(len(S))}
print(d)

s='abcd'
l=[10,20,30]
d={key:value for key,value in zip(s,l)}
print(d)



from itertools import zip_longest
s='abcd'
l=[10,20,30]
print(list(zip_longest(s,l, fillvalue='sai')))






















