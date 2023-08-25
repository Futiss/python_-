##with open('pi_digits.txt') as file_object:
##    contents = file_object.read()
##
##print(contents)
##print(contents.rstrip())    #rstrip()可以删除字符串末尾的空白
##
### 文件路径有 相对路径（相对于当前运行的程序所在的目录）与 绝对路径（文件在计算机中的准确位置）
##
##with open('pi_digits.txt') as file_object:
##    for line in file_object:
##        print(line)
##
##with open('pi_digits.txt') as file_object:
##    for line in file_object:
##        print(line.rstrip())
##
##

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())