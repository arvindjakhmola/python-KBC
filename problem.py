print("python program for that calculate the sutudents marks")
sub1 = int(input("Enter you marks of sub 1"))
sub2 = int(input("Enter you marks of sub 2"))
sub3 = int(input("Enter you marks of sub 3"))
sub4 = int(input("Enter you marks of sub 4"))
sub5 = int(input("Enter you marks of sub 5"))
totalmarks = sub1+sub2+sub3+sub4+sub5
print("your total marks are",totalmarks)
percentage = (totalmarks/100)*100 #we assume the paper was of 100 marks of each subject
print(f'your percentage is {percentage}%')
if percentage >=90:
    print("you will get grade A+")
elif percentage >=80:
    print("your will get grade A")
elif percentage >=70:
    print("your will get grade B")
elif percentage >=60:
    print("your will get grade C")
elif percentage>=50:
    print("your will get grade D")
else: 
    print("you are fail")