#GM1*m2/r**2

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

print(GREEN+"Calculator to calculate the numerical values based on Gravitation")
print("1 - To find M1")
print("2 - To find M2")
print("3 - To find r²")
print("4 - To find Force"+RESET)

find =(BLUE+ int(input("Enter the quantity you want to find: "))+RESET)

# Universal Gravitational Constant
ugc = 6.67 * 10**-11  
#1 for M1
if find == 1: 
    force = float(input("Enter Force (N): "))
    distance = float(input("Enter Distance/Radius (m): "))
    mass2 = float(input("Enter Mass of second object (kg): "))
    mass1 = (force * distance**2) / (ugc * mass2)
    print(BLUE+f"Mass m1 = {mass1} kg"+RESET)
#2 for m2
elif find == 2:
    force = float(input("Enter Force (N): "))
    distance = float(input("Enter Distance/Radius (m): "))
    mass1 = float(input("Enter Mass of first object (kg): "))
    mass2 = (force * distance**2) / (ugc * mass1)
    print(BLUE+f"Mass m2 = {mass2} kg"+RESET)
# 3 for r2
elif find == 3:
    force = float(input("Enter Force (N): "))
    mass1 = float(input("Enter Mass of first object (kg): "))
    mass2 = float(input("Enter Mass of second object (kg): "))
    r_squared = (ugc * mass1 * mass2) / force
    print(BLUE+f"Distance squared (r²) = {r_squared} m²"+RESET)
# 4 for Force
elif find == 4:
    mass1 = float(input("Enter Mass of first object (kg): "))
    mass2 = float(input("Enter Mass of second object (kg): "))
    distance = float(input("Enter Distance/Radius (m): "))
    force = (ugc * mass1 * mass2) / (distance**2)
    print(BLUE+f"Gravitational Force = {force} N"+RESET)

else:
    print(RED+"Invalid option! Please enter a number between 1 and 4."+RESET)
