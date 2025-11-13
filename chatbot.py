# Funtions below
products = [{'Product': 'Snickers', 'Price': 1.99},{'Product': 'Case of 40 waters', 'Price': 5.38} , {'Product': 'Single water bottle', 'Price': 0.75}, {'Product': 'Noodle Cups', 'Price': 1.82}]

def beginning():
    print("Welcome to HEB chat bot!")
    name = input("What is your name? ")
    age = input(f"Nice to meet you, {name}! How old are you? ")
    print(f"Welcome {name}! Wow you're {age}! You are so young! How can I help you today?")
    return name, age

def display_menu():
    print("\n Please choose from the Please choose from the following options:")
    print(" 1. Store Hours \n 2. Closes location to you \n 3. available products \n 4. Prices \n 5. Exit Conversation")

def selection(name):
    number = int(input('Enter the number of your choice[1-5]:  '))
    if number == 1:
        store_hourly()
    elif number == 2:
        location()
    elif number == 3:
        print_products()
    elif number == 4:
        price_of_product()
    elif number == 5:
        print(f"Have a great day! Goodbye, {name}!")
        return 1


def store_hourly():
    print('All store hours are from 6:00 AM till 11 PM')

def location():
    print('The closest location is at 10100 Beechnut St')

def print_products():
    for i in range(len(products)):
        print("---------------------")
        print(f"Product:{products[i]['Product']}")
    print("-------------------")

def price_of_product():
    for item in products:
        print("---------------------")
        for key, value in item.items():
            print(f"{key}:{value}")
    print("-------------------")



#commands below

name, age = beginning()
display_menu()
while selection(name) != 1:
    display_menu()

#hello world