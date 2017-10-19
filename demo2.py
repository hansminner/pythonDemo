# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
"""
a, b = 0, 1
while b < 10:
    # print(b)
    print(b, end=',')
    a, b = b, a + b
"""

# Python3 条件控制
# Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else
"""
注意：
1、每个条件后面要使用冒号（:），表示接下来是满足条件后要执行的语句块。
2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
3、在Python中没有switch – case语句。
"""

"""
var1 = 100
if var1:
    print("1-if 表达式条件为 true")
    print(var1)

var2 = 0
if var2:
    print("2-if 表达式条件为 true")
    print(var2)
print("good bye!")
"""

# 计算小狗的年龄
"""
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

### 退出提示
input("点击 enter 键退出")
"""

# if 嵌套
"""
num = int(input("enter a number:"))
if num % 2 == 0:
    if num % 3 == 0:
        print("the number can  be divided with no remainder by 2 and 3")
    else:
        print("the number only can  be divided with no remainder by 2")
else:
    if num % 3 == 0:
        print("the number only can  be divided with no remainder by 3")
    else:
        print("the number not can be divided with no remainder by 2 and 3")
"""

