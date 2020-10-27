name = "   my name is {name} And I am is {old}"
# print(name.capitalize())   #首字母大写

# print(name.lower())  #全部小写
#
# print(name.upper())   #全部大写

# print(name.count("l"))   #统计出现的次数
#
# print(name.center(50,'-'))   #用什么补全
#
# print(name.encode())   #编码
#
# print(name.endswith("ly"))  # 以什么结尾
#
# print(name.expandtabs(tabsize=30)) #指定tab键的长度

# print(name.find("y"))  # 可以用于切片 返回索引值
#
# print(name.format(name='billt',old=23))  # 格式化
#
# print(name.format_map({"name":"alex","old":"23"}))   #字典格式传参数

# print('abc'.isalnum()) # 是否是阿拉伯数字
#
# print('abc'.isalpha()) #是否是纯英文字符
#
# print('1a'.isdigit()) # 判断是否为整数

#print('abc'.isidentifier()) # 判断是不是一个合法的标识符(变量)

# print('My Name Is '.istitle())
#
# print('My Name Is '.isupper()) #判断是否都为大写
#
# print('-'.join(['1','2','3']))  # 将列表输出为字符串
#
# print(name.ljust(50,'*')) # 保证长度30 不够用*从尾端补全
#
# print(name.rjust(50,'-'))# 保证长度30 不够用*从头端补全

# print('\n\nname'.lstrip())  #去掉左边的换行符
#
# print('name\n\n'.rstrip())#去掉右边的换行符
#
# print('\n\nname\n\n'.strip())#去掉字符两端的换行符
'''
p = str.maketrans('abcdefghijk','!@#$%^&*()_')
print('jack'.translate(p))
将jack 每个字母按照上面字母对应的符号进行加密
'''
# print('alex li'.replace('l','L',1)) #替换字符
#
# print('alex li'.rfind('l'))  # 找到最右边的值得索引
#
# print('alex li'.split(' ')) #将字符串指定的分隔符分隔成列表
#
# print('alex\n l\ni'.splitlines())  #分隔符为换行符 分隔
#
# print('Alex Li'.swapcase())  #大写边小写  小写变大写
#
# print('lex li'.title()) #将字符串变成一个tittle  首字母大写
#
# print('alex li'.zfill(50)) # 用0 补全


