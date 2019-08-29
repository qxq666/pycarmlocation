class 成绩单():
    @classmethod
    def 录入成绩单(cls):
        cls.学生姓名 = input('请输入学生姓名：')
        cls.语文_成绩 = int(input('请输入语文成绩：'))
        cls.数学_成绩 = int(input('请输入数学成绩：'))
    @classmethod
    def 打印成绩单(cls):
        print(cls.学生姓名 + '的成绩单如下：')
        print('语文成绩：'+ str(cls.语文_成绩))
        print('数学成绩：'+ str(cls.数学_成绩))
成绩单.录入成绩单()
成绩单.打印成绩单()


#类的实例化：
class 成绩单():
    def 录入成绩单(self):
        self.学生姓名 = input('请输入学生姓名：')
        self.语文_成绩 = int(input('请输入语文成绩：'))
        self.数学_成绩 = int(input('请输入数学成绩：'))
    def 打印成绩单(self):
        print(self.学生姓名 + '的成绩单如下：')
        print('语文成绩：'+ str(self.语文_成绩))
        print('数学成绩：'+ str(self.数学_成绩))
成绩单1 = 成绩单() # 实例化，得到实例对象“成绩单1”
成绩单2 = 成绩单() # 实例化，得到实例对象“成绩单2”
成绩单3 = 成绩单() # 实例化，得到实例对象“成绩单2”


#未实例化代码
class 成绩单():
    @classmethod
    def 录入成绩单(cls):
        cls.学生姓名 = input('请输入学生姓名：')
        cls.语文_成绩 = int(input('请输入语文成绩：'))
        cls.数学_成绩 = int(input('请输入数学成绩：'))

    @classmethod
    def 打印成绩单(cls):
        print(cls.学生姓名 + '的成绩单如下：')
        print('语文成绩：'+ str(cls.语文_成绩))
        print('数学成绩：'+ str(cls.数学_成绩))

成绩单.录入成绩单()
成绩单.打印成绩单()


# 实例化之后
class 成绩单():   # ①不用再写@classmethod
    def 录入成绩单(self):  # ②cls变成self
        self.学生姓名 = input('请输入学生姓名：')  # ③cls.变成self.
        self.语文_成绩 = int(input('请输入语文成绩：'))
        self.数学_成绩 = int(input('请输入数学成绩：'))

    def 打印成绩单(self):
        print(self.学生姓名 + '的成绩单如下：')
        print('语文成绩：'+ str(self.语文_成绩))
        print('数学成绩：'+ str(self.数学_成绩))
成绩单1 = 成绩单() # ④创建实例对象：成绩单1
成绩单1.录入成绩单() # ⑤实例化后使用
成绩单1.打印成绩单()


#报错
class 智能机器人():
    胸围 = 33
    腰围 = 44
    臀围 = 55
    def 自报三围(self):
        print('主人，我的三围是：')
        print('胸围：' + str(self.胸围))
        print('腰围：' + str(self.腰围))
        print('臀围：' + str(self.臀围))
        print('哈哈哈哈哈，下面粗上面细，我长得像个圆锥。')
# 实例化后，直接使用类方法会报错
智能机器人.自报三围()


# 实例名可以与类名相同
class 成绩单():
    def 录入成绩单(self):
        self.学生姓名 = input('请输入学生姓名：')
        self.语文_成绩 = int(input('请输入语文成绩：'))
        self.数学_成绩 = int(input('请输入数学成绩：'))
    def 打印成绩单(self):
        print(self.学生姓名 + '的成绩单如下：')
        print('语文成绩：' + str(self.语文_成绩))
        print('数学成绩：' + str(self.数学_成绩))
成绩单 = 成绩单()  # 【请注意这里取了一个和类名相同的实例名】
成绩单.录入成绩单()
成绩单.打印成绩单()


#实例属性和类属性一致
class 类():
    变量 = 100
实例1 = 类() # 实例化
实例2 = 类() # 实例化
print(类.变量)
print(实例1.变量)
print(实例2.变量)


#【修改】类属性，实例属性也发生变化
class 类():
    变量 = 100
实例1 = 类() # 实例化
实例2 = 类() # 实例化
print(实例1.变量)
print(实例2.变量)
类.变量 = 'abc'   # 修改类属性
print(实例1.变量)   # 实例属性同步变化
print(实例2.变量)   # 实例属性同步变化


#仅【修改】实例属性，仅修改的实例变化，其余实例和类属性均不变
class 类():
    变量 = 100
实例1 = 类() # 实例化
实例2 = 类() # 实例化
print('原先的类属性：')
print(类.变量)
print('原先的实例1属性：')
print(实例1.变量)
print('原先的实例2属性：')
print(实例2.变量)

实例1.变量 = 'abc' #修改实例1的属性
print('--------修改实例1的属性后----------')
print(实例1.变量)


#【新增】类属性
class 类():
    变量1 = 100
实例 = 类() # 实例化
类.变量2 = 'abc' # 新增【类属】性
print(实例.变量1)
print(实例.变量2)

#新增实例属性，类属性不会变，代码会报错
class 类():
    变量1 = 100
实例 = 类() # 实例化
实例.变量2 = 'abc' # 新增实例属性
print(类.变量2)


#修改类方法，实例方法自动被修改例1
class 类():
    def 原始函数(self):
        print('我是原始函数！')
    def 新函数(self):
        print('我是重写后的新函数!')
a = 类()  # 实例化
a.原始函数()
类.原始函数 = 新函数 # 用新函数代替原始函数，也就是【重写类方法】
a.原始函数()# 现在原始函数已经被替换了

##修改类方法，实例方法自动被修改例2
class 幸运():
    def 好运翻倍(self):
         print('好的，我把它存了起来，然后翻了666倍还给你：' + str(self.幸运数 *666))
def 新好运翻倍(self):
    print('我是重写后的新函数')
    print('好的，我把它存了起来，然后翻了666倍还给你：' + str(self.幸运数 *666))
幸运.幸运数 = int(input('你的幸运数是多少？请输入一个整数。'))
幸运.好运翻倍=新好运翻倍
实例=幸运()
实例.好运翻倍()


#实例不能重写方法，会报错
class 幸运():
    def 好运翻倍(self):
        print('好的，我把它存了起来，然后翻了888倍还给你：' + str(self.幸运数*888))
def 新好运翻倍(self):
    print('我是重写后的新函数!')
    print('好的，我把它存了起来，然后翻了666倍还给你：' + str(self.幸运数*666))
幸运.幸运数 = int(input('你的幸运数是多少？请输入一个整数。'))
实例 = 幸运()  # 实例化
实例.好运翻倍 = 新好运翻倍    # 尝试重写实例方法，将会报错
实例.好运翻倍()


#初始化函数
class 类():
    def __init__(self):
        print('实例化成功！')
实例 = 类(


#初始化函数可以传递参数
class 成绩单():
    def __init__(self,学生姓名,语文_成绩,数学_成绩):
        self.学生姓名 = 学生姓名
        self.语文_成绩 = 语文_成绩
        self.数学_成绩 = 数学_成绩
    def 打印成绩单(self):
        print(self.学生姓名 + '的成绩单如下：')
        print('语文成绩：'+ str(self.语文_成绩))
        print('数学成绩：'+ str(self.数学_成绩))
成绩单1 = 成绩单('张三',99,88)
成绩单2 = 成绩单('李四',64,73)
成绩单3 = 成绩单('王五',33,22)
成绩单1.打印成绩单()
成绩单2.打印成绩单()
成绩单3.打印成绩单(


#九九乘法表
for i in range(1,10):
    for x in range(1,i+1):
        print( '%d X %d = %d' % (i ,x ,i*x) ,end = '  ' )
    print(' ')

#乘法表封装
class 乘法表():
    def __init__(self,n):
        self.n=n
    def 打印(self):
        for i in range(1,self.n+1):
            for x in range(1,i+1):
                print('%d X %d = %d' % (i, x, i * x), end='  ')
            print('  ')
三三乘法表 = 乘法表(3)
三三乘法表.打印()
五五乘法表 = 乘法表(5)
五五乘法表.打印()


#继承，子类完全继承父类
class 父类():
    def __init__(self,参数):
        self.变量 = 参数
    def 打印属性(self):
        print('变量的值是：')
        print(self.变量)
class 子类(父类):
    pass  # pass语句代表“什么都不做”
子类实例 = 子类(2)
子类实例.打印属性(


#继承，子类在父类的基础上有所改进
class 基础机器人():
    def __init__(self,参数):
        self.姓名=参数
    def 自报姓名(self):
        print('我是' + self.姓名 + '！')
    def 卖萌(self):
        print('主人，求抱抱！')
class 高级机器人(基础机器人):
    def 高级卖萌(self):
        print('主人，每次想到怎么欺负你的时候，就感觉自己全身biubiubiu散发着智慧的光芒！')
安迪=高级机器人('安迪')
安迪.自报姓名()
安迪.卖萌()
安迪.高级卖萌()


#继承，子方法覆盖父类方法
class 基础机器人():
    def __init__(self,参数):
        self.姓名 = 参数
    def 自报姓名(self):
        print('我是' + self.姓名 + '！')
    def 卖萌(self):
        print('主人，求抱抱！')
class 高级机器人(基础机器人):
    def 卖萌(self):  # 这里使用了相同的类方法名称“卖萌”，这样可以让子类方法覆盖父类方法
        print('主人，每次想到怎么欺负你的时候，就感觉自己全身biubiubiu散发着智慧的光芒！')
鲁宾 =  基础机器人('鲁宾')
鲁宾.自报姓名()
鲁宾.卖萌()
鲁宾 =  高级机器人('鲁宾')
鲁宾.自报姓名()
鲁宾.卖萌()

#继承，子类方法覆盖父类方法
class 基础机器人():
    def __init__(self,参数):
        self.姓名 = 参数
    def 自报姓名(self):
        print('我是' + self.姓名 + '！')
    def 卖萌(self):
        print('主人，求抱抱！')
class 高级机器人(基础机器人):
    def 自报姓名(self):
        print('我是高级机器人' + self.姓名 + '！')
    def 卖萌(self):
        print('主人，每次想到怎么欺负你的时候，就感觉自己全身biubiubiu散发着智慧的光芒！')
安迪 = 高级机器人('安迪')
安迪.自报姓名()
安迪.卖萌()

#继承
class 基础机器人():
    def __init__(self, 参数):
        self.姓名 = 参数
    def 自报姓名(self):
        print('我是' + self.姓名 + '！')
    def 卖萌(self):
        print('主人，求抱抱！')
class 高级机器人(基础机器人):
    def __init__(self,参数1,参数2):
        self.姓名=参数1
        self.智商=参数2
    def 自报姓名(self):
        print('我是' + self.姓名 + '！'+'智商高达' + str(self.智商) + '！')
    def 卖萌(self):
        print('主人，每次想到怎么欺负你的时候，就感觉自己全身biubiubiu散发着智慧的光芒！')
安迪 = 高级机器人('安迪', 150)
安迪.自报姓名()
安迪.卖萌()


#项目实操
class 出租车():
    def 计费(self):
        公里数 = float(input('请输入行程公里数：'))
        费用 = 公里数 * 2.5
        print('费用一共是：' + str(费用) + '元')
小王的出租车 = 出租车()
小王的出租车.计费()

#1、添加初始化函数
class 出租车():
    def __init__(self,参数):
        self.每公里费用 = 参数
    def 计费(self):
        公里数 = float(input('请输入行程公里数：'))
        费用 = 公里数 * self.每公里费用
        print('费用一共是：' + str(费用) + '元')

小王的出租车 = 出租车(2.5)
小王的出租车.计费()
小李的出租车 = 出租车(3)
小李的出租车.计费()

#2、前3公里15元，后面每公里2.5元
class 出租车():
    def __init__(self,参数):
        self.每公里费用 = 参数
    def 计费(self):
        公里数 = float(input('请输入行程公里数：'))
        if 公里数>3:
            费用 = (公里数-3) * self.每公里费用+15
            print('费用一共是：' + str(费用) + '元')
        else:
            print('费用一共是：15元')

小王的出租车 = 出租车(2.5)
小王的出租车.计费()

#3、有时候想改成4公里20元，有时候想改成2公里12元
class 出租车():
    def __init__(self,参数1,参数2,参数3):
        self.每公里费用 = 参数1
        self.前几公里=参数2
        self.前几公里费用=参数3
    def 计费(self):
        公里数 = float(input('请输入行程公里数：'))
        if 公里数<=self.前几公里:
            费用=self.前几公里费用
        else:
            费用= 15 + (公里数 - 3) *self.每公里费用
        print('费用一共是：' + str(费用) + '元')
小王的出租车 = 出租车(2.5, 3, 15)
小王的出租车.计费()

#4、重构代码，把计费函数拆解成计费、记录行程、统计费用、结算信息四个函数
class 出租车():
    def __init__(self, 参数1, 参数2, 参数3):
        self.每公里费用 = 参数1
        self.最低公里 = 参数2
        self.最低费用 = 参数3
    def 计费(self):
        self.记录行程()
        self.统计费用()
        self.结算信息()
    def 记录行程(self):
        self.公里数 = float(input('请输入行程公里数：'))
    def 统计费用(self):
        if self.公里数<=self.最低公里:
            self.费用=self.最低费用
        else:
            self.费用= 15 + (self.公里数 - 3) *self.每公里费用
    def 结算信息(self):
        print('费用一共是：' + str(self.费用) + '元')
小王的出租车 = 出租车(2.5, 3, 15)
小王的出租车.计费()

#5、开电动车的，现在政府号召环保，对电动车也补贴，所有电动车计费按8折算（继承）
class 出租车():
    def __init__(self, 参数1, 参数2, 参数3):
        self.每公里费用 = 参数1
        self.最低公里 = 参数2
        self.最低费用 = 参数3
    def 计费(self):
        self.记录行程()
        self.统计费用()
        self.结算信息()
    def 记录行程(self):
        self.行程公里数 = float(input('请输入行程公里数：'))
    def 统计费用(self):
        if self.行程公里数 <= self.最低公里:
            self.最终费用 = self.最低费用
        else:
            self.最终费用 = self.最低费用 + (self.行程公里数 - self.最低公里) * self.每公里费用
    def 结算信息(self):
        print('费用一共是：' + str(self.最终费用) + '元')

class 电动车(出租车):
    def 结算信息(self):
        print('费用一共是：' + str(self.最终费用*0.8) + '元')

小王的出租车 = 出租车(2.5, 3, 15)
小王的出租车.计费()

小李的电动车 = 电动车(2.5, 3, 15)
小李的电动车.计费()


#练习2
class Person:
    def __init__(self, name):
        self.name = name
        print('大家注意了！')
    def show(self):
        print('一个叫“%s”的人来了。' % self.name)
class Man(Person):
    def __init__(self):
        Person.__init__(self, name='范罗苏姆')  # 继承的基础上做一些改变
        # 上面的括号里也可以写成(self,'范罗苏姆')，但加上参数后清晰一些，代码看起来更清晰。
    def show(self):
        Person.show(self)  # 完全继承父类的方法
    def leave(self):  # 子类定制新方法
        print('那个叫“%s”的男人留下了他的背影。' % self.name)
author1 = Person('吉多')
author1.show()
author2 = Man()
author2.show()
author3 = Man()
author3.leave()
#结束