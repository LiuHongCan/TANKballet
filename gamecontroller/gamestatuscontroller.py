import pygame
import sys
from common.bullet import Bullet
from common.playertank import PlayerTank
from config.colorset import ColorSeting
from data.datalist import DataList
from gamelevels.levelsinit import LevelInit


class StatusController:
    def __init__(self):
        self.levelinit = LevelInit()


    def getevent(self):
        eventlist = pygame.event.get()
        for event in eventlist:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and not DataList.TANK_P1:
                    DataList.TANK_P1 = PlayerTank(400, 300)
                    self.levelinit.createplayertank()
                    DataList.TANK_P1.dispalytank()
                if DataList.TANK_P1 and DataList.TANK_P1.live:
                    if event.key == pygame.K_LEFT:
                        print("坦克向左移动")
                        DataList.TANK_P1.direction = 'LEFT'
                        DataList.TANK_P1.stop = False
                    elif event.key == pygame.K_RIGHT:
                        print("坦克向右移动")
                        DataList.TANK_P1.direction = 'RIGHT'
                        DataList.TANK_P1.stop = False
                    elif event.key == pygame.K_UP:
                        print("坦克向上移动")
                        DataList.TANK_P1.direction = 'UP'
                        DataList.TANK_P1.stop = False
                    elif event.key == pygame.K_DOWN:
                        print("坦克向下移动")
                        DataList.TANK_P1.direction = 'DOWN'
                        DataList.TANK_P1.stop = False
                    elif event.key == pygame.K_SPACE:
                        if len(DataList.BULLET_LIST) < 3:
                            m = Bullet(DataList.TANK_P1)
                            DataList.BULLET_LIST.append(m)
                        else:
                            print("子弹不足")
                        print("当前屏幕中的子弹数量为:{}".format(len(DataList.BULLET_LIST)))
            # 结束游戏的方法
            if event.type == pygame.KEYUP:
                # 松开的如果是方向键，改变移动状态
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    if DataList.TANK_P1 and DataList.TANK_P1.live:
                        DataList.TANK_P1.stop = True
    # 左上角绘制文字
    def gettextsurface(self, text):
        # 初始化字体模块
        pygame.font.init()
        font = pygame.font.SysFont('kaiti', 18)
        textsurface = font.render(text, True, ColorSeting.COLOR_RED)
        return textsurface

if __name__ == '__main__':
    pass

