def calAdd(a,b):
    return a+b

i =calAdd(12,33)
print(i)

# def upper(name):
#     return name.upper()

# print(upper("mandy"))

# def lower(name):
#      print(name.lower())

# n = "MANDY"

# lower(n)

# # print(n)

# def GreetName(name):
#     print("hello",name["fname"])

# name[fname="mandy"]

# GreetName(name)


def avg(*num):
    sum=0
    for i in num:
        sum=sum+i
    print(sum)

avg(4,5,6,7,8,8)