#cubes
# c=[i**3 for i in range(1,11)]
# print(c)


# #from the given tuple add only even numbers into the list

# T=(11,78,32,44,5,3,2,467,786)
# even=[i for i in T if i%2==0]
# print(even)
#
# # #from the given tuple add only odd numbers into the list
#
# T=(11,78,32,44,5,3,2,467,786)
# odd=[i for i in T if i%2==1]
# print(odd)

#
# T=(11,78,32,44,5,3,2,467,786)
# odd_even=[i for i in T if i%2==0 or i%2==1 and i>100  ]
# # or
# odd_even1=[i for i in T if i%2==0 and i>100]
# print(odd_even)
# print(odd_even1)


# Based on given numbers present in given tuple add one into the list if it is even otherwise add 0
# normal approach
# T=(11,78,32,44,5,3,2,467,786)
# L=[]
# for i in T:
#     if i%2==0:
#         L.append(1)
#     if i%2!=0:
#         L.append(0)
# print(L)
#
# # list comprehension approach
# T=(11,78,32,44,5,3,2,467,786)
# L=[1 if i%2==0 else 0 for i in T]
# print(L)


#value,multiple for loops and if condition
#syntax: [values for loop 1 for loop2 ……..for loop n  If condition]


#
# L=[[i,j,k] for i in range(1,6) for j in range(1,6) for k in range(1,6)  if i==j==k ]
# print(L)

# or

# L=[[i]*3 for i in range(1,6)]
# print(L)

































