# a = input("Enter the number ")
# print("MULTIPLICATION TABLE OF ",a)

# try:
#     for i in range(1,10):
#         print(f"{a} * {i} = {int(a)*i }  ")
# except Exception as e :
#     print(e)

a = int(input("ENter a value between 1 to 10 \t"))

if( a > 10 ):
    raise ValueError("value is > 10 ")