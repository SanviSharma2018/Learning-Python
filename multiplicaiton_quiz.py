import random

print("Welcome to the multiplication quiz!")

num_1 = random.randint(1, 11)
num_2 = random.randint(1, 11)

answer = int(input(f"What is {num_1} x {num_2} ? "))

if answer == num_1 * num_2:
    print("Correct! good")
else:
    print("Wrong!")
