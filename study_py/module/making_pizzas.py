'''
两种导入方式：
    1、
    import module_name

    module_name.function_name()

    2、
    from module_name import function_name
    多个：from module_name import function_0, function_1, function_2

    function_name()
'''

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12,'mushrooms', 'green peppers', 'extra cheese')

# 使用星号（*）可以导入模块中所有函数(最好别用)
from pizza import *
make_pizza(16, 'pepperoni')



