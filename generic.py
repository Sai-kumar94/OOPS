
class Bank:
    bank_name='sbi'
    bank_ifsc=1234
    bank_address='andhra'
vivek=Bank()
sai=Bank()

#Accessing of generic properties by using class
#syntax:
        #ClassName.classvariable
print(Bank.bank_name)
print(Bank.bank_ifsc)


#Accessing of generic properties by using object
#syntax:
        #Objectname.classvariable
print(vivek.bank_name)
print(sai.bank_ifsc)


#modifying of generic properties by using class
#syntax:
        #ClassName.classvariable=Newvalue
Bank.bank_ifsc=4567
print(Bank.bank_ifsc)
print(vivek.bank_ifsc)
print(sai.bank_ifsc)



#note:

# if we modify generic property by using class then it modifies
# in class and as well as objects


#modifying of generic properties by using object
#syntax:
        #ObjectName.classvariable=Newvalue
vivek.bank_address='telangana'
print(Bank.bank_address)
print(vivek.bank_address)
print(sai.bank_address)

# if we modify generic property by using OBJECT  then it modifies
# in only tha particular object


#deleting of generic properties by using class
#syntax:
        # del ClassName.classvariable
del Bank.bank_ifsc
print(Bank.bank_ifsc)
print(vivek.bank_ifsc)
print(sai.bank_ifsc)

# NOTE: if we delete generic property by using class then it deletes
# in class and as well as objects


#  Deleting generic property by using OBJECT
# NOTE:
# we cannot delete generic property by using Object


# Creating generic properties by using class
# syntax:
        #ClassName.Newclassvariable=value
Bank.bank_mobile=234567890
print(Bank.bank_mobile)
print(vivek.bank_mobile)
print(sai.bank_mobile)

# if we create generic property by using class then it create in class and object


# creating generic property by using object
# note
# we cannot create generic property by using object


