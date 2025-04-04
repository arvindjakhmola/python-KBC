def average(*numbers):  # Accepts any number of arguments
    # print(type(numbers))  # (commented out) would show numbers is a tuple

    sum = 0  # Initialize sum to 0
    for i in numbers:  # Iterate through all arguments
        sum = sum + i  # Add each number to sum
        print("Average is: ", sum / len(numbers))  # Prints inside loop (incorrect) 
        print ("enter unit ") 
or phir float wgera lgaad