"""通过的测试"""
# def get_formatted_name(first, last):
#     """生成整洁的姓名。"""
#     full_name = f"{first} {last}"
#     return full_name.title()

# """11.1.3 未通过的测试"""
# def get_formatted_name(first, middle, last):
#     """生成整洁的姓名。"""
#     full_nmae = f"{first} {middle} {last}"
#     return full_nmae.title()

"""添加if测试"""
def get_formatted_name(first, last,  middle=''):
    """生成整洁的姓名。"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
