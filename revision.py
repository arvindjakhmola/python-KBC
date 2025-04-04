# a = "welcome to the game"
# print(a.title().center(100,"."))
#                          #this is the best methon to put on heddings 
# print(a.count("t"))
# str1 = "World Health Organization" 
# print(str1.istitle())


print("what is your name and class and roll no.")
name = input("please enter your name").strip().lower()
if name == "arvind":
    print("ok arvind now enter your password")
    password = input(">")
    if password == "arvindjakhmola":
         print("yes your are the user")
else:
     print ("wrong user")
