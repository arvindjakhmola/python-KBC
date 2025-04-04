print("Kon banega karod pati".upper().center(50))

print("Price for per points are \n1. 1Point = 1cr \n2. 2Point for 2cr\n3. 3Point for 3cr\n4. 4Point for 4cr\n5. 5Point for 5cr")

questions = [
    "Which planet is known as the Red Planet?",
    "Who wrote the national anthem of India?",
    "What is the capital of Japan?",
    "How many continents are there on Earth?",
    "Which is the longest river in the world?"
]

answers = [
    "mars",
    "rabindranath tagore",
    "tokyo",
    "seven",
    "nile river"
]

count = 0

# First question
print("First question is\n", questions[0])
ans0 = input("Please write your answer > ").lower().strip()
if ans0 == answers[0]:
    print("Correct answer!")
    count += 1
else:
    print("Wrong answer, your points will not be lost.")

# Second question
print("Your second question is", questions[1])
ans1 = input("> ").lower().strip()
if ans1 == answers[1]:
    print("Correct answer!")
    count += 1
else:
    print("Wrong answer, your points will not be lost.")

# Third question
print("Your third question is", questions[2])
ans2 = input("> ").lower().strip()
if ans2 == answers[2]:
    print("Correct answer!")
    count += 1
else:
    print("Wrong answer, your points will not be lost.")

# Fourth question
print("Your fourth question is", questions[3])
ans3 = input("> ").lower().strip()
if ans3 == answers[3] or 7 :
    print("Correct answer!")
    count += 1
else:
    print("Wrong answer, your points will not be lost.")

# Fifth question
print("Your fifth question is", questions[4],"please write answer like this ___river")
ans4 = input("> ").lower().strip()
if ans4 == answers[4]:
    print("Correct answer!")
    count += 1
else:
    print("Wrong answer, your points will not be lost.")

# Display the final score
print("So your points are", count, "therefore you will get:")
if count == 1:
    print("Congratulations, you have won 1cr!")
elif count == 2:
    print("Congratulations, you have won 2cr!")
elif count == 3:
    print("Congratulations, you have won 3cr!")
elif count == 4:
    print("Congratulations, you have won 4cr!")
elif count == 5:
    print("Congratulations, you have won 5cr!")
else:
    print("Unfortunately, you won nothing this time!")

# if code is giving error sremove strip()