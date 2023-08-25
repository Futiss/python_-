#banned_users = ['andrew','carolina','david']
#user = 'marie'
#
#if user not in banned_users:
#    print(f"{user.upper()}, you can post a response if you wish.")

#age = 19
#if age >= 18:
#    print("You are old enough to vote!")
#
#age = 19
#if age >= 18:
#    print("You are old enough to vote!")
#    print("Have you registered to vote yet?")
#else:
#    print("You are still a baby!")
#
#
#age = 12
#
#if age <4:
#    print("Your admission cost is $0.")
#elif age < 18:
#    print("Your admission cost is $25.")
#else:
#    print("Your admission cost is $40.")
#
#age = 19
#
#if age < 4:
#    price = 0
#elif age < 18:
#    price = 25
#elif age < 65:
#    price = 40
#elif age >= 65:
#    price = 20
#
#print(f"Your admission cost is ${price}.")

available_toppings = ['mushrooms','olives','green peppers',
                      'pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in  requested_toppings:
    if requested_topping in available_toppings:
        print (f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")