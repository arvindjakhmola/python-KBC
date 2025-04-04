import time
print("time greeter")
usertime = int(time.localtime().tm_hour)
# print("your current time is ",usertime)
if (usertime > 1):
    print("Good Moning")
elif(usertime > 13):
    print("Good Evinging sir")
elif (usertime > 23):
    print("Good Night sir")
else:
    print("I don't know what time it is")

# 1=13    
# 2=14
# 3=15
# 4=16
# 5=17
# 12=24
# 11=23
# 10=22