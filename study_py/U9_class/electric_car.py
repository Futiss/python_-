from car import Car

class Battery:
    """一次模拟电动汽车电瓶的简单尝试。"""

    def __init__(self, battery_size=75):
        """初始化电瓶的属性。"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程。"""
        if self.battery_size ==75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):                              #必须在圆括号内指定父类的名称。
    """电动汽车的独特之处。"""

    def __init__(self, make, model, year):           #方法__init_()接受创建Car实例所需的信息
        """初始化父类的属性。
        再初始化电动汽车特有的属性。
        """
        super().__init__(make, model, year)          #super()是一个特殊函数，让我们可以调用父类的方法。父类也称为超类（superclass），也即名字由来。
        self.battery = Battery()

    #重写父类方法，假设Car中有fill_gas_tank()的方法：
    def fill_gas_tank(self):
        """电动汽车没有油箱。"""
        print("This car doesn't need a gas tank!")

