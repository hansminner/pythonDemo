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

# 迭代器 iter() 和 next()。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

# 迭代器对象可以使用常规for语句进行遍历：
"""
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")
"""
# 也可以使用 next() 函数：
"""
import sys  # 引入 sys 模块

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
"""

# 生成器 yield 使用了 yield 的函数被称为生成器（generator）
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回yield的值。
# 并在下一次执行 next()方法时从当前位置继续运行。
"""
一个函数 f，f 返回一个 list，这个 list 是动态计算出来的（不管是数学上的计算还是逻辑上的读取格式化），
并且这个 list 会很大（无论是固定很大还是随着输入参数的增大而增大），
这个时候，我们希望每次调用这个函数并使用迭代器进行循环的时候一个一个的得到每个 list 元素而不是直接得到一个完整的 list 来节省内存，
这个时候 yield 就很有用。
"""

"""
import sys

def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
"""