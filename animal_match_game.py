import random
animals = ["cat", "camel", "monkey", "elephant"]

computer_selection = random.choice(animals)
print(computer_selection)
user_selection = input("Enter your animal name ")

if user_selection == computer_selection:
    print("yay! it matchs good job!!!")
else:
    print("Our choice doesnt match")
