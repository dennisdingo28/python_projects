name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right, which way would you like to go?").lower()

if answer=="left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim across: ")

elif answer=="right":
    print()
else:
    print("Not a valid option. You lose.")