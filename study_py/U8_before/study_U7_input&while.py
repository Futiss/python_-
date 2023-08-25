message = input("Tell me your secret, son.")
print(message)


prompt = "If you tell us who you are, we can personaalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"\nHello, {name}!")
#
#number = input("Enter a number, and I'll tell you if it's even or odd: ")
#number = int(number)
#
#if number % 2 == 0:
#    print(f"\nThe number {number} is even.")
#else:
#    print(f"The number {number} is odd.")



#current_number = 1
#while current_number <= 5:
#    print(current_number)
#    current_number += 1

#prompt = "\nTell me something, and I will repeat it back to you:"
#prompt += "\nEnter 'quit' to end the program. "
#message = ""
#while message != 'quit':
#    message = input(prompt)
#    print(message)


#prompt = "\nTell me something, and I will repeat it back to you:"
#prompt += "\nEnter 'quit' to end the program. "
#
#active = True
#while active:
#    message = input(prompt)
#
#    if message == 'quit':
#        active = False
#    else:
#        print(message)

#prompt = "\nPlease enter the name of a city you have visited:"
#prompt += "\n(Enter 'quit' when you are finished.)"
#
#while True:
#    city = input(prompt)
#
#    if city == 'quit':
#        break
#    else:
#        print(f"I'd love to go to {city.title()}!")

#current_number = 0
#while current_number <=10:
#    current_number += 1
#    if current_number %2 == 0:
#        continue
#
#    print(current_number)

#x = 1
#while x <= 5:
#    print(x)
#    x += 1

#prompt = "Please add your toppings:"
#toppings = []
#
#while True:
#    topping = input(prompt)
#    if topping == 'quit':
#        break
#    else:
#        toppings.append(topping)
#        print(f"we'll add {topping} on the pizza.")
#
#print("\nYour pizza have:")
#for topping in toppings:
#    print(topping)

#while True:
#    age = input("请输入观众的年龄（输入'quit'结束）：")
#    if age == 'quit':
#        break
#    age = int(age)
#    if age < 3:
#        print("观众免费入场。")
#    elif age <= 12:
#        print("观众需要支付10美元的票价。")
#    else:
#        print("观众需要支付15美元的票价。")

#while True:
#    print("这是一个没完没了的循环。按Ctrl + C结束循环。")

#unconfirmed_users = ['alice', 'brian', 'candace']
#confirmed_users = []
#
#while unconfirmed_users:
#    current_user = unconfirmed_users.pop()
#    print(f"Verifying user: {current_user.title()}")
#    confirmed_users.append(current_user)
#
#print("\nThe following users have been confirmed:")
#for confirmed_user in confirmed_users:
#    print(confirmed_user.title())


#unconfirmed_users = ['alice', 'brain', 'candace']
#confirmed_users = []
#
#while unconfirmed_users:
#    current_user = unconfirmed_users.pop()
#    print(f"Verifying user: {current_user.title()}")
#    confirmed_users.append(current_user)
#
#print("\nThe following users have been confirmed:")
#for confirmed_user in confirmed_users:
#    print(confirmed_user.title())

#pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
#print(pets)
#
#while 'cat' in pets:
#    pets.remove('cat')
#
#print(pets)


responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response

    repeat = input("Would you like to let another person respond?(yes/no) ")
    if repeat == 'no':
        polling_active = False
    
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}. ")


