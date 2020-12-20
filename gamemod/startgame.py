import time
import pygame
from common.readiniconfig import ReadIniData
from config.colorset import ColorSeting
from data.datalist import DataList
from gamecontroller.gamestatuscontroller import StatusController
from gamelevels.levelsinit import LevelInit


class MainGame():
    # 游戏主窗口
    def __init__(self):
        # 初始化pygame
        self.display = pygame.display
        self.levelinit = LevelInit()
        self.controller = StatusController()

        self.COLOR_BACK = pygame.Color(ColorSeting().COLOR_BLACK)
        self.COLOR_RED = pygame.Color(ColorSeting().COLOR_RED)
        self.SCREEN_HEIGHT = ReadIniData().getwindowsize()[0]
        self.SCREEN_WIDTH = ReadIniData().getwindowsize()[1]
        self.window = DataList.window
        # 我方坦克
        self.TANK_P1 = DataList.TANK_P1
        # 敌方坦克列表
        self.ENEMYTANK_LIST = DataList.ENEMYTANK_LIST
        # 敌方坦克总数
        self.ENEMYTANK_COUNT = DataList.ENEMYTANK_COUNT
        # 储存我方子弹列表
        self.BULLET_LIST = DataList.BULLET_LIST
        # 储存敌方子弹列表
        self.ENEMY_BULLET_LIST = DataList.ENEMY_BULLET_LIST
        # 爆炸效果列表
        self.EXPLODE_LIST = DataList.EXPLODE_LIST
        # 墙壁列表
        self.WALL_LIST = DataList.WALL_LIST
        # 版本号
        self.VERSION = DataList.VERSION

    def StartGame(self):
        self.display.init()
        print(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        MainGame.window = self.display.set_mode([int(self.SCREEN_WIDTH), int(self.SCREEN_HEIGHT)])
        DataList.window = MainGame.window
        # 创建玩家坦克
        self.levelinit.createplayertank()
        self.TANK_P1 = DataList.TANK_P1
        # 创建敌人坦克
        self.levelinit.createenemytank()
        self.ENEMYTANK_LIST = DataList.ENEMYTANK_LIST
        # 创建墙壁
        self.levelinit.createwalls()
        # 设置窗口标题
        self.display.set_caption('坦克大战' + self.VERSION)

        while True:
            # 窗口背景色填充
            MainGame.window.fill(self.COLOR_BACK)
            # 获取游戏事件
            self.controller.getevent()
            MainGame.window.blit(self.controller.gettextsurface("剩余敌方坦克%d辆"%len(self.ENEMYTANK_LIST)),(5,5))
            # 调用展示墙壁的方法
            self.levelinit.blitwalls(MainGame.window)
            if self.TANK_P1 and self.TANK_P1.live:
                # 将我方坦克加入窗口
                self.TANK_P1.dispalytank()
            else:
                del DataList.TANK_P1
                DataList.TANK_P1 = None
                self.TANK_P1 = DataList.TANK_P1
            # 循环展示敌方坦克
            # self.levelinit.blitenemytank()
            self.ENEMYTANK_LIST = DataList.ENEMYTANK_LIST
            # 根据坦克的开关状态调用坦克的移动方法
            if self.TANK_P1 and not self.TANK_P1.stop:
                self.TANK_P1.tankmove()
            # 调用渲染子弹列表的方法
            self.levelinit.blitbullet()
            # 调用渲染敌方子弹的方法
            self.levelinit.blitenemybullet()
            # 调用展示爆炸效果的方法
            self.levelinit.displayexplodes()

            time.sleep(0.02)
            self.display.update()
if __name__ == '__main__':
    MainGame().StartGame()
    # print(MainGame().SCREEN_WIDTH)
    pass