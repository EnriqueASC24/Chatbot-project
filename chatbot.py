# Funtions below

def beginning():
    print("Welcome to Elite 101 Chatbot!")
    name = input("What is your name? ")
    age = input(f"Nice to meet you, {name}! How old are you? ")
    print(f"Welcome {name}! Wow you're {age}! You are so young! How can I help you today?")
    return name, age

def display_menu():
    print("\n Please choose from the Please choose from the following options:")
    print(" 1. Place holder for option 1\n 2. Place holder for option 2\n 3. Place holder for option 3\n 4. Exit Conversation")

def selection(name):
    number = int(input('Enter the number of your choice: '))
    if number == 1:
        print("Place holder for option 1")
    elif number == 2:
        print("Place holder for option 2")
    elif number == 3:
        print("Place holder for option 3")
    elif number == 4:
        print(f"Have a great day! Goodbye, {name}!")
        return 1

#commands below

name, age = beginning()
display_menu()
while selection(name) != 1:
    display_menu()

#hello world