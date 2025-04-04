def force(M,m,r):
    G = 6.67*10**-11
    F = G * (M * m) / r**2
    print(F)   

def Mass1(m,r,F):
    G = 6.67*10**-11
    M = (F*r**2)/(G*m)
    print(M)

def mass2(M,F,r):
    G = 6.67*10**-11
    m =  (F*r**2)/(G*M)
    print(m)

def distance(M,m,F):
    G = 6.67*10**-11
    r = ((G * M * m) / F) ** 0.5
    print(r)   

print("Calculator to calculate the numerical values based on Gravitation")
print("1 - To find force")
print("2 - To find mass 1")
print("3 - To find mass 2")
print("4 - To find distane")

find = int(input(">"))

if find == 1:
    M = float(input("Enter mass1"))
    m = float(input("Enter mass2"))
    r = float(input("Enter distance"))
    force(M,m,r)
elif find == 2:
    m = float(input("Enter mass2"))
    r = float(input("Enter distance"))
    F = float(input("Enter force"))
    Mass1(m,r,F)
elif find == 3:
    M = float(input("Enter mass1"))
    r = float(input("Enter distance"))
    F = float(input("Enter force"))
    mass2(M,F,r)
elif find == 4:
    F = float(input("Enter force"))
    M = float(input("Enter mass1"))
    m = float(input("Enter mass2"))
    distance(M,m,F)