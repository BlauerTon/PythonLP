num1 = input("What is your first number")
num2 = input("What is the second number")
opps = input ("What operation would you like to perform\n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n")

num1 = int(num1)
num2 = int(num2)
opps = int(opps)



if opps == 1:
    print(num1 + num2)
elif opps == 2:
    print(num1 - num2)
elif opps == 3:
    print(num1 * num2)
elif opps == 4:
    print(num1 / num2)
else:
    print("Invalid Selection")
