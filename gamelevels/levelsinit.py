import random
import pygame
from common.enemytank import EnemyTank
from common.musicmethod import Music
from common.playertank import PlayerTank
from common.wallmethod import Wall
from data.datalist import DataList


class LevelInit():
    # def __init__(self):
    #     # self.window = window


    # 创建玩家坦克
    def createplayertank(self):
        # 实例化玩家坦克
        DataList.TANK_P1 = PlayerTank(400, 300)
        # 创建音乐对象
        music = Music('start.wav')
        # 调用音乐播放
        music.playmusic()
    def createenemytank(self):
        top = 100
        for i in range(DataList.ENEMYTANK_COUNT):
            speed = random.randint(3, 6)
            left = random.randint(1, 7)
            etank = EnemyTank(left*100, top, speed)
            DataList.ENEMYTANK_LIST.append(etank)
    def createwalls(self):
        for i in range(6):
            wall = Wall(130*i, 240)
            DataList.WALL_LIST.append(wall)
    def blitwalls(self, window):
        for wall in DataList.WALL_LIST:
            if wall.live:
                wall.displaywall(window)
            else:
                DataList.WALL_LIST.remove(wall)
    # 绘制敌方坦克
    def blitenemytank(self):
        for enemtank in DataList.ENEMYTANK_LIST:
            if enemtank.live:
                enemtank.dispalytank()
                enemtank.randmove()
                enemtank.collisionplayertank()
                enemtank.hitwalls()
                ebullet = enemtank.shot()
                # 如果子弹为空，则不加入列表
                if ebullet:
                    DataList.ENEMY_BULLET_LIST.append(ebullet)
            else:
                DataList.ENEMYTANK_LIST.remove(enemtank)
    # 绘制我方子弹
    def blitbullet(self):
        for bullet in DataList.BULLET_LIST:
            if bullet.live:
                bullet.displaybullet()
                # 让子弹动
                bullet.bulletmove()
                # 调用我方子弹与敌方坦克碰撞的方法
                bullet.hitenemytank()
                # 调用我方子弹是否碰到墙壁的方法
                bullet.hitwall()
            else:
                DataList.BULLET_LIST.remove(bullet)
    # 绘制敌方子弹
    def blitenemybullet(self):
        for ebullet in DataList.ENEMY_BULLET_LIST:
            # 如果子弹还活着，则绘制，否则从列表移除
            if ebullet.live:
                ebullet.dispalybullet()
                ebullet.bulletmove()
                ebullet.hitwall()
                if DataList.TANK_P1 and DataList.TANK_P1.live:
                    ebullet.hitplayertank()
            else:
                DataList.ENEMY_BULLET_LIST.remove(ebullet)
    # 展示爆炸
    def displayexplodes(self):
        for explode in DataList.EXPLODE_LIST:
            if explode.live:
                explode.displayexplode()
            else:
                DataList.EXPLODE_LIST.remove(explode)


if __name__ == '__main__':
    pass




