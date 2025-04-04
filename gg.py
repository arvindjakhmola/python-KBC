# def calculate (a,b):
#     cal = (a+b)*(a-b)
#     print(cal)
# calculate(v,c)
a = int(input("enter any number"))
b = int(input("enter another number"))

def isless(a,b):
    if a<b:
        print("second no. is greater")
    else:
        print("fist no. is greater")

isless(a,b)