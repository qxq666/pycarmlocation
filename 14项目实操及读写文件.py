#未封装成类的版本
import time, random

# 需要的数据和变量放在开头
player_list = ['【狂血战士】', '【森林箭手】', '【光明骑士】', '【独行剑客】', '【格斗大师】', '【枪弹专家】']
enemy_list = ['【暗黑战士】', '【黑暗弩手】', '【暗夜骑士】', '【嗜血刀客】', '【首席刺客】', '【陷阱之王】']
players = random.sample(player_list, 3)
enemies = random.sample(enemy_list, 3)
player_info = {}
enemy_info = {}


# 随机生成角色的属性
def born_role():
    life = random.randint(100, 180)
    attack = random.randint(30, 50)
    return life, attack


# 生成和展示角色信息
def show_role():
    for i in range(3):
        player_info[players[i]] = born_role()
        enemy_info[enemies[i]] = born_role()

    # 展示我方的3个角色
    print('----------------- 角色信息 -----------------')
    print('你的人物：')
    for i in range(3):
        print('%s  血量：%s  攻击：%s'
              % (players[i], player_info[players[i]][0], player_info[players[i]][1]))
    print('--------------------------------------------')
    print('电脑敌人：')

    # 展示敌方的3个角色
    for i in range(3):
        print('%s  血量：%s  攻击：%s'
              % (enemies[i], enemy_info[enemies[i]][0], enemy_info[enemies[i]][1]))
    print('--------------------------------------------')
    input('请按回车键继续。\n')  # 为了让玩家更有控制感，可以插入类似的代码来切分游戏进程。


# 角色排序，选择出场顺序。
def order_role():
    global players
    order_dict = {}
    for i in range(3):
        order = int(input('你想将 %s 放在第几个上场？(输入数字1~3)' % players[i]))
        order_dict[order] = players[i]

    players = []
    for i in range(1, 4):
        players.append(order_dict[i])

    print('\n我方角色的出场顺序是：%s、%s、%s' % (players[0], players[1], players[2]))
    print('敌方角色的出场顺序是：%s、%s、%s' % (enemies[0], enemies[1], enemies[2]))


# 角色PK
def pk_role():
    round = 1
    score = 0
    for i in range(3):  # 一共要打三局
        player_name = players[i]
        enemy_name = enemies[i]
        player_life = player_info[players[i]][0]
        player_attack = player_info[players[i]][1]
        enemy_life = enemy_info[enemies[i]][0]
        enemy_attack = enemy_info[enemies[i]][1]

        # 每一局开战前展示战斗信息
        print('\n----------------- 【第%s局】 -----------------' % round)
        print('玩家角色：%s vs 敌方角色：%s ' % (player_name, enemy_name))
        print('%s 血量：%s  攻击：%s' % (player_name, player_life, player_attack))
        print('%s 血量：%s  攻击：%s' % (enemy_name, enemy_life, enemy_attack))
        print('--------------------------------------------')
        input('请按回车键继续。\n')

        # 开始判断血量是否都大于零，然后互扣血量。
        while player_life > 0 and enemy_life > 0:
            enemy_life = enemy_life - player_attack
            player_life = player_life - enemy_attack
            print('%s发起了攻击，%s剩余血量%s' % (player_name, enemy_name, enemy_life))
            print('%s发起了攻击，%s剩余血量%s' % (enemy_name, player_name, player_life))
            print('--------------------------------------------')
            time.sleep(1)
        else:  # 每局的战果展示，以及分数score和局数的变化。
            # 调用show_result()函数，打印返回元组中的result。
            print(show_result(player_life, enemy_life)[1])
            # 调用show_result()函数，完成计分变动。
            score += int(show_result(player_life, enemy_life)[0])
            round += 1
    input('\n点击回车，查看比赛的最终结果\n')

    if score > 0:
        print('【最终结果：你赢了！】\n')
    elif score < 0:
        print('【最终结果：你输了！】\n')
    else:
        print('【最终结果：平局！】\n')


# 返回单局战果和计分法所加分数。
def show_result(player_life, enemy_life):  # 注意：该函数要设定参数，才能判断单局战果。
    if player_life > 0 and enemy_life <= 0:
        result = '\n敌人死翘翘了，你赢了！'
        return 1, result  # 返回元组(1,'\n敌人死翘翘了，你赢了！')，类似角色属性的传递。
    elif player_life <= 0 and enemy_life > 0:
        result = '\n悲催，敌人把你干掉了！'
        return -1, result
    else:
        result = '\n哎呀，你和敌人同归于尽了！'
        return 0, result


# （主函数）展开战斗流程
def main():
    show_role()  # 生成和展示角色信息
    order_role()  # 角色排序，选择出场顺序
    pk_role()  # 完成角色PK，并展示PK结果


# 启动程序（即调用主函数）
main()




#封装后版本
import random
import time
# 创建一个类，可实例化成具体的游戏角色
class Role():
    def __init__(self, name='【角色】'):  # 把角色名作为默认参数
        self.name = name
        self.life = random.randint(100, 150)
        self.attack = random.randint(30, 50)
# 创建三个子类，可实例化为3个不同类型的角色
class Knight(Role):
    def __init__(self, name='【圣光骑士】'):  # 把子类角色名作为默认参数
        Role.__init__(self, name)  # 利用了父类的初始化函数
        self.life = self.life * 5  # 骑士有5份血量
        self.attack = self.attack * 3  # 骑士有3份攻击力
class Assassin(Role):
    def __init__(self, name='【暗影刺客】'):
        Role.__init__(self, name)
        self.life = self.life * 3
        self.attack = self.attack * 5
class Bowman(Role):
    def __init__(self, name='【精灵弩手】'):
        Role.__init__(self, name)
        self.life = self.life * 4
        self.attack = self.attack * 4
# 创建一个类，可生成3V3并展示：可分为：欢迎语→随机生成→展示角色
class Game:
    def __init__(self):
        # 初始化各种变量
        self.players = []
        self.enemies = []
        self.score = 0
        # 执行各种游戏函数
        self.game_start()
        self.born_role()
        self.show_role()
    # 欢迎语
    def game_start(self):
        print('------------ 欢迎来到“PK小游戏” ------------')
        print('将自动生成【玩家角色】和【电脑人物】')
        input('请按回车键继续。')
    # 随机生成6个角色
    def born_role(self):
        self.life = random.randint(100, 180)
        self.attack = random.randint(30, 50)

        # 展示角色
        def show_role(self):
            print('----------------- 角色信息 -----------------')
            print('你的队伍：')
            for i in range(3):
                print('『我方』%s 血量：%s  攻击：%s' %
                      (self.players[i].name, self.players[i].life, self.players[i].attack))
            print('--------------------------------------------')

            print('敌人队伍：')
            for i in range(3):
                print('『敌方』%s 血量：%s  攻击：%s' %
                      (self.enemies[i].name, self.enemies[i].life, self.enemies[i].attack))
            print('--------------------------------------------')
gp = Game()  # 运行游戏

#编码
print('吴枫'.encode('utf-8'))
print('吴枫'.encode('gbk'))
#解码
print(b'\xe5\x90\xb4\xe6\x9e\xab'.decode('utf-8'))
print(b'\xce\xe2\xb7\xe3'.decode('gbk'))
#查看类型
print(type('吴枫'))
print(type(b'\xce\xe2\xb7\xe3'))

print(b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0'.decode('utf-8'))

print('K'.encode('ASCII'))

#读取文件
file1 = open('C:\\Users\\qxq\\Desktop\\abc.txt','r',encoding='utf-8')
filecontent = file1.read()
print(filecontent)
file1.close()

#写入文件
file1 = open('C:\\Users\\qxq\\Desktop\\abc.txt','a',encoding='utf-8')
file1.write('张无忌\n')
file1.write('宋青书\n')
file1.close()

#写入并读取
file1=open('C:\\Users\\qxq\\Desktop\\abc.txt','a',encoding='utf-8')
file1.write('难念的经')
file1.close()

file1=open('C:\\Users\\qxq\\Desktop\\abc.txt','r',encoding='utf-8')
filecontent=file1.read()
print(filecontent)
file1.close()

#读取文件并分别计算四个人成绩总和
#读
file1=open('C:\\Users\\qxq\\Desktop\\scores.txt','r',encoding='utf-8')
file_lines =file1.readlines()
file1.close()
#读出并计算
final_scores=[]
for i in file_lines:
    data=i.split()
    sum=0
    for score in data[1:]:
        sum=sum+int(score)
    result=data[0]+str(sum)+'\n'
    final_scores.append(result)
#写入
winner=open('C:\\Users\\qxq\\Desktop\\scores.txt','w',encoding='utf-8')
winner.writelines(final_scores)
winner.close()



