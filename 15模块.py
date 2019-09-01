#所有调用方式的简单展示
a = '我是模块中的变量a'
def hi():
    a = '我是函数里的变量a'
    print('函数“hi”已经运行！')
class Go1:  # 如果没有继承的类，class语句中可以省略括号，但定义函数的def语句括号不能省
    a = '我是类1中的变量a'
    @classmethod
    def do1(cls):
        print('函数“do1”已经运行！')
class Go2:
    a = '我是类2中的变量a'
    def do2(self):
        print('函数“do2”已经运行！')
print(a)  # 打印变量“a”
hi()  # 调用函数“hi”

print(Go1.a)  # 打印类属性“a”
Go1.do1()  # 调用类方法“Go1”

A = Go2()  # 实例化“Go2”类
print(A.a)  # 打印实例属性“a”
A.do2()  # 调用实例方法“do2”



#导入模块

# 这是主程序main.py
# 请阅读代码注释
import test  # 导入test模块

print(test.a)  # 使用“模块.变量”调用模块中的变量

test.hi()  # 使用“模块.函数()”调用模块中的函数

print(test.Go1.a)   # 使用“模块.类.变量”调用模块中的类属性
test.Go1.do1()  # 使用“模块.类.函数()”调用模块中的类方法

A = test.Go2()  # 使用“变量 = 模块.类()”实例化模块中的类
print(A.a)  # 实例化后，不再需要“模块.”
A.do2()  # 实例化后，不再需要“模块.”


#实例
sentence = '从前有座山，'
def mountain():
    print('山里有座庙，')
class Temple:
    sentence = '庙里有个老和尚，'
    @classmethod
    def reading(cls):
        print('在讲故事，')
class Story:
    sentence = '一个长长的故事。'
    def reading(self):
        print('讲的什么故事呢？')
for i in range(10):#重复10遍
    print(sentence)
    mountain()
    print(Temple.sentence)
    Temple.reading()
    A = Story()
    print(A.sentence)
    A.reading()
    print()
#将上述代码拆分
#story文件存放封装好的变量、函数与类
sentence = '从前有座山，'
def mountain():
    print('山里有座庙，')
class Temple:
    sentence = '庙里有个老和尚，'
    @classmethod
    def reading(cls):
        print('在讲故事，')
class Story:
    sentence = '一个长长的故事。'
    def reading(self):
        print('讲的什么故事呢？')
#main文件存放执行语句
import story
for i in range(10):
    print(story.sentence)
    story.mountain()
    print(story.Temple.sentence)
    story.Temple.reading()
    A = story.Story()
    print(A.sentence)
    A.reading()
    print()
#仅打印类Temple的属性
from story import Temple
print(Temple.sentence)


#关于random模块
import random  # 调用random模块

a = random.random()  # 随机从0-1之间抽取一个小数
print(a)

a = random.randint(0,100)  # 随机从0-100之间抽取一个数字
print(a)

a = random.choice('abcdefg')  # 随机从字符串/列表/字典等对象中抽取一个元素（可能会重复）
print(a)

a = random.sample('abcdefg', 3) # 随机从字符串/列表/字典等对象中抽取多个不重复的元素
print(a)

items = [1, 2, 3, 4, 5, 6]  # “随机洗牌”，比如打乱列表
random.shuffle(items)
print(items)


#用dir查看模块
import random  # 调用random模块
print(dir(random))
a = ''  # 设置一个字符串
print('字符串：')
print(dir(a))    # 把字符串相关的函数展示出来
a = []  # 设置一个列表
print('列表：')
print(dir(a))    # 把列表相关的函数展示出来
a = {}  # 设置一个字典
print('字典：')
print(dir(a))  # 把字典相关的函数展示出来



#CSV模块的学习
import csv
# dir()函数会得到一个列表，用for循环一行行打印列表比较直观
for i in dir(csv):
    print(i)


#读取CSV文件
import csv
with open("C:\\Users\\qxq\\Desktop\\test.csv",newline = '')  as f:
    reader = csv.reader(f)
    #使用csv的reader()方法，创建一个reader对象
    for row in reader:
    #遍历reader对象的每一行
        print(row)
print("读取完毕！")

#写入CSV
import csv
with open("C:\\Users\\qxq\\Desktop\\test.csv",'a',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['4', '猫砂', '25', '1022', '886'])
print('写入完毕')



