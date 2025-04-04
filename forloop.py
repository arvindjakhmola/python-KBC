# for k in range (0,37,3):
#     # print(k)
#     x = k/36
#     print(x)
#     # print("this is probablity of getting a multiple of 3 while throwing a dice",x) 
# for char in "Python":
#     print(char)

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

i = int(input("enter any number"))
while (i > 100):
  i = int(input(RED+"enter any number"+RESET))
  print (RED+"this is not a number i wanted"+RESET)
  if i > 59:
    print(YELLOW+"number is greater then what i want"+RESET)
  elif i < 59:
    print(YELLOW+"your guessed number is smaller"+RESET)
  else: 
    i == 59
    print("ooh man you guessed it write")
    print(GREEN + "thanks for playing my game".upper().center(50, ".") + RESET)
    