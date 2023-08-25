"""
    unittest模块中有6个常用的断言方法：

    1、assertEqual(a, b)-------核实 a == b
    2、assertNotEqual(a, b)----核实 a != b
    3、assertTrue(x)-----------核实 x 为 True
    4、assertFalse(x)----------核实 x 为 False
    5、assertIn(item, list )---核实 item 在 list 中
    6、assertNotIn(item, list )---核实 item 不在 list 中

"""

# 一个帮助管理匿名调查的类：
class AnonymousSurvey:
    """收集匿名调查问卷的答案。"""

    def __init__(self, question):
        """存储一个问题，并为存储答案做准备。"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查答卷。"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答案。"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
# 379 (还是应该再学习一下关于类的“__init__()方法与 self ”)

