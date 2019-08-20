
#类的相关学习代码


def 加100函数(参数):
    总和 = 参数 + 100
    print('计算结果如下：')
    print(总和)
参数 = 1
加100函数(参数)

class 加100类():
    def 加100函数(参数):
        总和 = 参数 + 100
        print('计算结果如下：')
        print(总和)
参数 = 1
加100类.加100函数(参数)

class 智能机器人():
    胸围 = 33
    腰围 = 44
    臀围 = 55
    @classmethod
    def 自报三围(cls):
        print('主人，我的三围是：')
        print('胸围：' + str(cls.胸围))
        print('腰围：' + str(cls.腰围))
        print('臀围：' + str(cls.臀围))
        print('哈哈哈哈哈，下面粗上面细，我长得像个圆锥。')
智能机器人.自报三围()

class 念诗类():
    一首诗 = ['《卜算子》', '我住长江头，', '君住长江尾。', '日日思君不见君，', '共饮长江水。']
    @classmethod
    def 念诗函数(cls):
        for i in cls.一首诗:
            print(i)
念诗类.念诗函数()


class 加100类():
    变量 = 100
    @classmethod
    def 加100函数(cls, 参数):
        总和 = cls.变量 + 参数
        print('加100函数计算结果如下：')
        print(总和)

参数 = int(input('请输入一个整数：'))
加100类.加100函数(参数)


class 加100类():
    变量 = 100
    @classmethod
    def 加100函数(cls, 参数1, 参数2, 参数3):
        总和 = cls.变量 + 参数1 + 参数2 + 参数3
        print('加100函数计算结果如下：')
        print(总和)

参数1 = int(input('请输入一个整数：'))
参数2 = int(input('请输入一个整数：'))
参数3 = int(input('请输入一个整数：'))
加100类.加100函数(参数1, 参数2, 参数3)

import requests
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
#下载《三国演义》第一回，我们得到一个对象，它被命名为res
res.encoding='utf-8'
#定义Reponse对象的编码为utf-8
novel=res.text
#把Response对象的内容以字符串的形式返回
print(novel[:800])


class 念诗类():
    一首诗 = ['《卜算子》', '我住长江头，', '君住长江尾。', '日日思君不见君，', '共饮长江水。']
    @classmethod
    def 念诗函数(cls,参数):
        print('念给张三的诗')
        for i in cls.一首诗:
            print(i)
念诗类.念诗函数(参数)

class 类A():
    pass

类A.变量1 = 100
print(类A.变量1)

class 类():
    @classmethod
    def 打印类属性(cls):
        print(cls.变量)

类.变量 = input('请输入字符串：')
类.打印类属性()

class 小幸运():
    @classmethod
    def 幸运翻倍(cls):
        print('好的，我把它存了起来，然后翻了888倍还给你：'+str(cls.变量*888))
小幸运.变量=int(input('你的幸运数是多少？请输入一个整数。'))
小幸运.幸运翻倍()

#从外部增加类属性
class 类():
    @classmethod
    def 增加类属性(cls):
        cls.变量 = input('请随意输入字符串：')
类.增加类属性()
print('打印新增的类属性：')
print(类.变量)


class 念诗类():
    一首诗 = ['《卜算子》', '我住长江头，', '君住长江尾。', '日日思君不见君，', '共饮长江水。']
    @classmethod
    def 念诗函数(cls):
        cls.变量= input('请输入你想给谁念诗：')
        print('念给' + cls.变量 + '的诗：')
        for i in cls.一首诗:
            print(i)
念诗类.念诗函数(参数)





class 成绩单():
    @classmethod
    def 录入成绩单(cls):
        cls.学生姓名 = input('请输入学生姓名：')
        cls.语文_成绩 = int(input('请输入语文成绩：'))
        cls.数学_成绩=int(input('请输入数学成绩：'))
    @classmethod
    def 打印成绩单(cls):
        print(cls.学生姓名 + '的成绩单如下：')
        print('语文成绩：'+ str(cls.语文_成绩))
        print('数学成绩：' + str(cls.数学_成绩))
    @classmethod
    def 打印平均数(cls):
        cls.平均分=(cls.语文_成绩+cls.数学_成绩)/2
        print(cls.学生姓名+'的平均分是'+str(cls.平均分))
    @classmethod
    def 评级(cls):
        if cls.平均分>=90:
            print(cls.学生姓名+'的评级是：优 ')
        elif 80<= cls.平均分<90:
            print(cls.学生姓名+'的评级是：良 ')
        elif 60<= cls.平均分<80:
            print(cls.学生姓名+'的评级是：中 ')
        else:
            print(cls.学生姓名+'的评级是：差 ')

成绩单.录入成绩单()
成绩单.打印成绩单()
成绩单.打印平均数()
成绩单.评级()



class 成绩单():
    @classmethod
    def 录入成绩单(cls):
        cls.学生姓名 = input('请输入学生姓名：')
        cls.语文_成绩 = int(input('请输入语文成绩：'))
        cls.数学_成绩 = int(input('请输入数学成绩：'))

    @classmethod
    def 计算平均分(cls):
        平均分 = (cls.语文_成绩 + cls.数学_成绩)/2
        return 平均分

    @classmethod
    def 评级(cls):
        平均分 = cls.计算平均分()
        if 平均分>=90:
            print(cls.学生姓名 + '的评级是：优')
        elif 平均分>= 80 and 平均分<90 :
            print(cls.学生姓名 + '的评级是：良')
        elif 平均分>= 60 and 平均分<80 :
            print(cls.学生姓名 + '的评级是：中')
        else:
            print(cls.学生姓名 + '的评级是：差')

成绩单.录入成绩单()
成绩单.评级()



class 成绩单():
    @classmethod
    def 录入成绩单(cls):
        cls.学生姓名 = input('请输入学生姓名：')
        cls.成绩 = int(input('请输入考试成绩：'))

    @classmethod
    def 计算是否及格(cls):
        if cls.成绩 >= 60:
            return '及格'
        else:
            return '不及格'

    @classmethod
    def 考试结果(cls):
        判断=成绩单.计算是否及格()
        if 判断=='及格':
            print (cls.学生姓名+'同学考试通过啦！')
        else:
            print(cls.学生姓名+'同学需要补考')
成绩单.录入成绩单()
成绩单.考试结果()


class calendar:
    # 日程表的日期
    date = '2020-08-08'
    # 事件清单，以字典形式给出，键为事件，值是安排的时间
    things = {'给父母买礼物':'9:00', '学习':'10:00', '和朋友聚会':'18:30'}
    @classmethod
    def thing_done(cls, thing):
        del cls.things[thing]   #删除字典中的已完成的thing
    @classmethod
    def add_thing(cls, thing, time):
        cls.things[thing] = time       #给字典添加变量，thing为键，time为值
calendar.thing_done('给父母买礼物')    #给父母买礼物已完成，删除
calendar.add_thing('写日记', '20:00')   #添加新事项
print(calendar.things)    #将更新的类内的属性things打印