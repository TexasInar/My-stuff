import time # this imports the time module

print("Welcome to my integer calculator!")
print("What is your name?")
user_name = input()
print("Hey, " + user_name)

num1 = int(input("Please enter your first integer: "))
num2 = int(input("Now enter your second integer: "))
addition_result = num1 + num2
subtraction_result = num1 - num2

print(user_name + ", please enter 1 for addition \nor enter 2 for subtraction.")
user_choice = int(input())
if user_choice == 1:
    time.sleep(1)
    print(num1, " plus ", num2, " make ", addition_result)
elif user_choice == 2:
    time.sleep(1)
    print(num1, " minus ", num2, " makes ", subtraction_result)
else:
    print(user_name, ", why can't you do what I ask?")

time.sleep(2)
print("Thanks for using my calculator, ", user_name, "!")
