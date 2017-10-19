#!/usr/bin/python3

"""
input("\n\n按下 enter 键后退出。"),

import sys;x = 'runoob'; sys.stdout.write(x + '\n'),
"""
# number 支持4中类型

"""
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
"""

# 您也可以使用del语句删除一些对象引用。
"""
var1 = 1,
var2 = 10,
del var1
"""

# 数值的除法（/）总是返回一个浮点数，要获取整数使用//操作符。

# 索引值以 0 为开始值，-1 为从末尾的开始位置。

"""
str = 'Runoob'
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符 Runoo
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 连接字符串 RunoobTEST
"""

# 另外，反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 '''...''' 跨越多行。

# List （列表）list是一种有序的集合，可以随时添加和删除其中的元素。
"""
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']
 
print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表

['abcd', 786, 2.23, 'runoob', 70.2]
abcd
[786, 2.23]
[2.23, 'runoob', 70.2]
[123, 'runoob', 123, 'runoob']
['abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob']

"""
# List  python中的list是python的内置数据类型，list中的数据类不必相同的，而array的中的类型必须全部相同。\
# 在list中的数据类型保存的是数据的存放的地址，简单的说就是指针，并非数据，这样保存一个list就太麻烦了

"""
list1=[1,2,3,'a']  
print list1  
a=np.array([1,2,3,4,5])  
b=np.array([[1,2,3],[4,5,6]])  
c=list(a)   # array到list的转换  
print a,np.shape(a)  
print b,np.shape(b)  
print c,np.shape(c)  

[1, 2, 3, 'a'] # 元素数据类型不同，并且用逗号隔开  
[1 2 3 4 5] (5L,) # 一维数组，类型用tuple表示  
"""
# 与Python字符串不一样的是，列表中的元素是可以改变的：
"""
>>>a = [1, 2, 3, 4, 5, 6]
>>> a[0] = 9
>>> a[2:5] = [13, 14, 15]
>>> a
[9, 2, 13, 14, 15, 6]
>>> a[2:5] = []   # 删除
>>> a
[9, 2, 6]
"""
# Tuple（元组）
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改,一旦初始化就不能修改
# 元组写在小括号()里，元素之间用逗号隔开。
# 元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取（看上面，这里不再赘述）。
# 其实，可以把字符串看作一种特殊的元组。虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple

"""
>>> t = ('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])
"""
# 这个tuple定义的时候有3个元素，分别是'a'，'b'和一个list。不是说tuple一旦定义后就不可变了吗？怎么后来又变了？

# Set（集合）
# 集合（set）是一个无序不重复元素的序列。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

"""
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
 
print(student)   # 输出集合，重复的元素被自动去掉
 
# 成员测试
if('Rose' in student) :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a和b的差集
print(a | b)     # a和b的并集
print(a & b)     # a和b的交集
print(a ^ b)     # a和b中不同时存在的元素

{'Mary', 'Jim', 'Rose', 'Jack', 'Tom'}
Rose 在集合中
{'b', 'a', 'c', 'r', 'd'}
{'b', 'd', 'r'}
{'l', 'r', 'a', 'c', 'z', 'm', 'b', 'd'}
{'a', 'c'}
{'l', 'r', 'z', 'm', 'b', 'd'}
"""

# Dictionary（字典)
# 列表是有序的对象结合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

"""
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"
 
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
 
print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值
1 - 菜鸟教程
2 - 菜鸟工具
{'name': 'runoob', 'site': 'www.runoob.com', 'code': 1}
dict_keys(['name', 'site', 'code'])
dict_values(['runoob', 'www.runoob.com', 1])
"""
# 构造函数 dict() 可以直接从键值对序列中构建字典如下：
"""
>>>dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
{'Taobao': 3, 'Runoob': 1, 'Google': 2}
 
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
 
>>> dict(Runoob=1, Google=2, Taobao=3)
{'Taobao': 3, 'Runoob': 1, 'Google': 2}
"""
# Python赋值运算符
"""
a = 21
b = 10
c = 0

c //= a
print ("7 - c 的值为：", c)
"""

# not(a and b) 返回 False 假设变量 a 为 10, b为 20:
"""
if not( a and b ):
   print ("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
   print ("5 - 变量 a 和 b 都为 true")
"""
# Python成员运算符 in,not in
# Python身份运算符 is,is not

# Python三引号 python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
"""
para_str = \"""这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
\"""
print (para_str)

"""
