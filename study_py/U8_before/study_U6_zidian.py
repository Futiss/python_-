#  字典
#alien_0 = {'color':'green','points':5}
#
#new_points = alien_0['points']
#print(f"You just earned {new_points} points!")
#
#alien_1 = {}
#alien_1['color'] = 'green'
#alien_1['points'] = 5
#print(alien_1)

#alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
#print(f"Original position: {alien_0['x_position']}")
#
## 向右移动外星人
## 根据当前速度确定将外星人向右移动多远
#
#if alien_0['speed'] == 'slow':
#    x_increment = 1
#elif alien_0['speed'] == 'medium':
#    x_increment = 2
#else: 
#    #这个外星人速度肯定很快
#    x_increment = 3
#
#alien_0['x_position'] = alien_0['x_position'] + x_increment
#
#print(f"New position: {alien_0['x_position']}")
#
#del alien_0['speed']
#print(alien_0)
#
#point_value = alien_0.get('points', 'No point value assigned.')
#print(point_value)
#
#for key,value in alien_0.items():
#    print(f"\nKey:{key}")
#    print(f"Value:{value}")
#
#for key in alien_0.keys():
#    print("\n",key.title())

#favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'python',
#    }
#
#print("The following languages have been mentioned:")
#
#for language in favorite_languages.values():
#    print(language.title())
#
#print("\n")
#
#for language in set(favorite_languages.values()):
#    print(language.title())

#alien_0 = {'color': 'green', 'points':5}
#alien_1 = {'color': 'yellow', 'points':10}
#alien_2 = {'color': 'red', 'points':15}
#
#aliens = [alien_0, alien_1,alien_2]
#
#for alien in aliens:
#    print(alien)

#aliens = []
#for alien_number in range(30):
#    new_alien = {'color': 'green', 'points':5, 'speed':'slow'}
#    aliens.append(new_alien)
#
#for alien in aliens[:3]:
#    if alien['color'] == 'green':
#        alien['color'] = 'yellow'
#        alien['points'] = 10
#        alien['speed'] = 'medium'
#
#for alien in aliens[:5]:
#    print(alien)
#print("...")
#
#print(f"Total number of aliens:{len(aliens)}")

pizza = {
    'crust': 'thick',
    'toppings':['mushrooms','extra cheese'],
    }

print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

#for topping in pizza['toppings']:
#    print("\n"f+topping)
for topping in pizza['toppings']:
    print(f"\t {topping}")