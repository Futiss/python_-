#def greet_user():
#    '''显示简单的问候语。'''
#    print("Hello!")
#
#greet_user()
#
#
#def greet_user(username):  #username is a parameter(形参)
#    '''显示简单的问候语。'''
#    print(f"Hello, {username.title()}! ")
#
#greet_user('Jesse')        #'Jesse' is a argument(实参)
#
#def display_message():
#    '''指出本章学了什么'''
#    print("本章学习了: \n\t怎么定义函数、\n\t如何向函数传递信息、\n\t形参(parameter)实参(argument)是什么")
#
#display_message()
#
#
#def describe_pet(animal_type, pet_name):
#    '''显示宠物信息'''
#    print(f"\nI have a {animal_type}")
#    print(f"My {animal_type}'s name is {pet_name.title()}. ")
#
#describe_pet('hamster', 'harry')
#describe_pet('horse', 'peter')
#
#describe_pet(animal_type='hamster', pet_name='harry')
#describe_pet( pet_name='harry', animal_type='hamster')
#
#
#def describe_pet(pet_name, animal_type='dog'):
#    '''显示宠物信息'''
#    print(f"\nI have a {animal_type}.")
#    print(f"My {animal_type}'s name is {pet_name.title()}. ")
#
#describe_pet('harry')
#
#def make_shirt(size,message):
#    '''打印T恤的尺码和字样'''
#    print(f'The size of the T-shirt is {size}, message is "{message}". ')
#
#make_shirt('S', 'Just do it.')
#
#def get_formatted_name(first_name, last_name):
#    '''返回整洁的名字'''
#    full_name = f"\n{first_name} {last_name}"
#    return full_name.title()
#
#musician = get_formatted_name('jimi', 'hendrix')
#print(musician)
#
#
#def build_person(first_name, last_name):
#    '''返回一个字典，其中包含有关一个人的信息。'''
#    person = {'first': first_name, 'last': last_name}
#    return person
#
#musician = build_person('jimi', 'hendrix')
#print(musician)
#
#
#
#def build_person(first_name, last_name, age=None):
#    '''返回一个字典，其中包含有关一个人的信息。'''
#    person = {'first': first_name, 'last': last_name}
#    if age:
#        person['age'] = age
#    return person
#
#musician = build_person('jimi', 'hendrix', age=27)
#print(musician)



#def get_formatted_name(first_name, last_name):
#    '''返回整洁的名字'''
#    full_name = f"{first_name} {last_name}"
#    return full_name.title()
#
##  这是一个无限循环 ！
#while True:
#    print("\nPlease tell me your name: ")
#    f_name = input("First name:")
#
#    if f_name == "quit":
#        break
#    
#    l_name = input("Last name: ")
#
#
#    get_formatted_name = get_formatted_name(f_name, l_name)
#    print(f"\nHello, {get_formatted_name}!")


#def city_country(city, country):
#    '''返回城市及所属国'''
#    city_country = f"{city} {country}"  #该函数使用f-string将两字符串拼起来 
#    return city_country.title()
#
#while True:
#    print("\nPlease tell me the city: ")
#    city = input("city(Enter 'q' at any time to quit. ):")
#
#    if city == "q":
#        break
#
#    print("\nPlease inform us of the country: ")
#    country = input("country:")
#
#    city_country = city_country(city, country)
#    print(f'\n"{city_country}"')

#def greet_users(names):
#    '''向列表中的每位用户发出简单的问候。'''
#    for name in names:
#        msg = f"Hello, {name}! "
#        print(msg)
#
#usernames = ['hannah', 'ty', 'margot']
#greet_users(usernames)


#unprinted_designs = ['phone case', 'robot pendant', 'dodecahedorn']
#completed_models = []
#
#while unprinted_designs:
#    current_design = unprinted_designs.pop()
#    print(f"Printing moddel: {current_design}")
#    completed_models.append(current_design)
#
#print("\nThe following models have beeen printed: ")
#for completed_model in completed_models:
#    print(completed_model)

#def print_models(unprinted_designs, completed_models):
#    """
#    模拟打印每个设计，知道没有未打印的设计为止。
#    打印每个设计后, 都将其转移到列表completed_models中。
#    """
#    while unprinted_designs:
#        current_design = unprinted_designs.pop()
#        print(f"Printing model: {current_design}")
#        completed_models.append(current_design)
#
#def show_completed_models(compledted_models):
#    """显示打印好的所有模型"""
#    print("\nThe following models have been printed: ")
#    for completed_model in compledted_models:
#        print(completed_model)
#
#unprinted_designs = ['phone case', 'robot pendant', 'dogecahedron']
#completed_models = []
#
#print_models(unprinted_designs[:], completed_models)
#show_completed_models(completed_models)
#print(unprinted_designs)


#def make_pizza(*toppings):
#    '''打印顾客点的所有配料。'''
#    print(toppings)
#
#make_pizza('pe')
#make_pizza('a','s','d')


#def make_pizza(*toppings):          #   *创建元组
#    '''概述要制作的披萨。'''
#    print("\nMaking a pizza with the following toppings: ")
#    for topping in toppings:
#        print(f"- {topping}")
#
#make_pizza('pe')
#make_pizza('a','s','d')


#def make_pizza(size,*toppings):
#    '''概述要制作的披萨。'''
#    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
#    for topping in toppings:
#        print(f"- {topping}")
#
#make_pizza(16, 'pe')
#make_pizza(12, 'a','s','d')

#def build_profile(first,last, **user_info):     #   **创建空字典
#    """创建一个字典，其中包含我们知道的有关用户的一切。"""
#    user_info['first_name'] = first
#    user_info['last_name'] = last
#    return user_info
#
#user_profile = build_profile('a','b',location = 'c',field = 'd')    # ab位置实参，cd关键字实参
#print(user_profile)

