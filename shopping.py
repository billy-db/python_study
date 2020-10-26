# #
# __author__ = "Seven"

'''
流程思路
        1、用户输入金额
                1、输入的金额为数字且为整数。
                       1、获取商品的序号
                       2、用户输入商品序号进行判断
                            -1、用户输入的序号是为数字（整数）
                                    -1、用户输入的序号是在商品序号范围内
                                            用户金额与商品价格比较
                                                1、可以购买（将商品添加到用户购买成的列表，获取扣除商品价格后的余额）
                                                2、不可以购买（提示用户余额不足）
                                    -2、用户输入的序号不在商品序号范围内（提示用户范围）
                            -2、用户输入的序号是其他字符（提示用户）
                            -3、用户选择退出（打印出用户购买的商品，和余额）
                2、用户输入得不是数字（提示用户输入错误）
'''
product_list = [
    ('Iphone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('Alex Python',120),
]
shopping_list = []
salary = input("请输入你的金额:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for item in product_list:
            print(product_list.index(item),item)
        user_choice = input("选择你要买的商品序号,退出请输入quit：")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary: #买的起
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("\033[31;1m%s\033[0m购买成功,余额剩余\033[32;1m%s\033[0m" % (p_item,salary))
                else:
                    print("\033[32;1m你的余额只剩[%s]啦，还买个毛线\033[0m" % salary)
            else:
                print("输入的商品序号不存在，在请输入\033[34;1m{_index}\033[0m-\033[34;1m{_index2}\033[0m之间".format(_index=0,_index2=len(product_list)-1))
        elif user_choice == 'quit':
            print("--------您已经购买的商品------")
            for p in shopping_list:
                print("\033[35;1m{p}\033[0m".format(p=p))
            print("您的余额剩余:\033[32;1m%s\033[0m" % (salary))
            exit()
        else:
            print("输入商品序号无效")
else:
    print("输入错误，请输入金额")