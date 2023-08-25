filename = 'programming.txt'
#with open(filename, 'w') as file_object:        # 'w'是写入模式。
#    file_object.write("I love programming.\n")
#    file_object.write("I love creating new games.\n")

with open(filename, 'a') as file_object:        # 'a'附加模式。
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I also love creating apps that can run in a browser.\n")

