import fibo

# 模块
# 在前面的几个章节中我们脚本上是用 python 解释器来编程，如果你从 Python 解释器退出再进入，那么你定义的所有的方法和变量就都消失了。
# 为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。
# 模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。
"""
# 文件名: using_sys.py

import sys

print('命令行参数如下:')
for i in sys.argv:
   print(i)

print('\n\nPython 路径为：', sys.path, '\n')
"""

# import 语句
# 想使用 Python 源文件，只需在另一个源文件里执行 import 语句，语法如下：
"""
import module1[, module2[,... moduleN]
"""

"""
# 导入模块
import support
 
# 现在可以调用模块里包含的函数了
support.print_func("Runoob")
"""

"""
>>> fibo.fib(1000)
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
"""

# 如果你打算经常使用一个函数，你可以把它赋给一个本地的名称：
"""
>>> fib = fibo.fib
>>> fib(500)
1 1 2 3 5 8 13 21 34 55 89 144 233 377
"""

# from…import 语句

# Python的from语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：
"""
from modname import name1[, name2[, ... nameN]]
例如，要导入模块 fibo 的 fib 函数，使用如下语句：
>>> from fibo import fib, fib2
>>> fib(500)
1 1 2 3 5 8 13 21 34 55 89 144 233 377
"""

# From…import* 语句

# 把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
"""
from modname import *
"""
# 这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。

# 深入模块
# 模块除了方法定义，还可以包括可执行的代码。这些代码一般用来初始化这个模块。这些代码只有在第一次被导入时才会被执行。
# 每个模块有各自独立的符号表，在模块内部为所有的函数当作全局符号表来使用。

# __name__属性
# 一个模块被另一个程序第一次引入时，其主程序将运行。
# 如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
"""
# Filename: using_name.py

__main__ 就是当前模块的方法名,未引入时是当前的__name__是__main__,未引入就不一定了
if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')
运行输出如下：
$ python using_name.py
程序自身在运行
$ python
>>> import using_name
我来自另一模块
>>>
说明： 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
"""
# dir() 函数

"""
内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
</p>
<pre>
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
"""

# 如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称:
"""
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir() # 得到一个当前模块中定义的属性列表
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
>>> a = 5 # 建立一个新的变量 'a'
>>> dir()
['__builtins__', '__doc__', '__name__', 'a', 'sys']
>>>
>>> del a # 删除变量名a
>>>
>>> dir()
['__builtins__', '__doc__', '__name__', 'sys']
>>>
"""

# 标准模块
# Python 本身带着一些标准的模块库，在 Python 库参考文档中将会介绍到（就是后面的"库参考文档"）。
# 有些模块直接被构建在解析器里，这些虽然不是一些语言内置的功能，但是他却能很高效的使用，甚至是系统级调用也没问题。
# 这些组件会根据不同的操作系统进行不同形式的配置，比如 winreg 这个模块就只会提供给 Windows 系统。
# 应该注意到这有一个特别的模块 sys ，它内置在每一个 Python 解析器中。变量 sys.ps1 和 sys.ps2 定义了主提示符和副提示符所对应的字符串:

# 包
# 包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
# 比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B 。
# 就好像使用模块的时候，你不用担心不同模块之间的全局变量相互影响一样，采用点模块名称这种形式也不用担心不同库之间的模块重名的情况。

"""
sound/                          顶层包
      __init__.py               初始化 sound 包
      formats/                  文件格式转换子包
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  声音效果子包
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  filters 子包
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
"""
# 在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录。
# 目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包

"""
# 用户可以每次只导入一个包里面的特定模块，比如:
import sound.effects.echo
这将会导入子模块:sound.effects.echo。 他必须使用全名去访问:
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
# 还有一种导入子模块的方法是:
from sound.effects import echo
这同样会导入子模块: echo，并且他不需要那些冗长的前缀，所以他可以这样使用:
echo.echofilter(input, output, delay=0.7, atten=4)
# 还有一种变化就是直接导入一个函数或者变量:
from sound.effects.echo import echofilter
同样的，这种方法会导入子模块: echo，并且可以直接使用他的 echofilter() 函数:
echofilter(input, output, delay=0.7, atten=4)
"""

# 注意当使用from package import item这种形式的时候，对应的item既可以是包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量。
# import语法会首先把item当作一个包定义的名称，如果没找到，再试图按照一个模块去导入。如果还没找到，恭喜，一个:exc:ImportError 异常被抛出了。
# 反之，如果使用形如import item.subitem.subsubitem这种导入形式，除了最后一项，都必须是包，而最后一项则可以是模块或者是包，但是不可以是类，函数或者变量的名字。

# 从一个包中导入* 不推荐
# 设想一下，如果我们使用 from sound.effects import *会发生什么？
# 为了解决这个问题，只能烦劳包作者提供一个精确的包的索引了。
# 导入语句遵循如下规则：如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。
# 可别忘了在更新包之后保证 __all__ 也更新了啊。我就不使用导入*这种用法，。这里有一个例子，在:file:sounds/effects/__init__.py中包含如下代码:
# __all__ = ["echo", "surround", "reverse"]
# 这表示当你使用from sound.effects import *这种用法时，你只会导入包里面这三个子模块。
# __all__=["modualA","modualB"] 暴露接口 在model __inti__里都可以用

# 无论是隐式的还是显式的相对导入都是从当前模块开始的。主模块的名字永远是"__main__"，一个Python应用程序的主模块，应当总是使用绝对路径引用。
# 包还提供一个额外的属性__path__。这是一个目录列表，里面每一个包含的目录都有为这个包服务的__init__.py，你得在其他__init__.py被执行前定义哦。
# 可以修改这个变量，用来影响包含在包里面的模块和子包。
# 这个功能并不常用，一般用来扩展包里面的模块。
