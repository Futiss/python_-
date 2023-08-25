filename = 'pi_digits.txt'

with open(filename) as file_object: #直接读取为字符串，需要使用float()转化为浮点数，或int()转化为整数
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()   #rstrip()去除末尾空格，strip()去除空格

print(pi_string)
print(len(pi_string))

print(f"{pi_string[:52]}...")
print(len(pi_string))