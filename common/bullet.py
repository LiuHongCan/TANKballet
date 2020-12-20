import pygame
from common.explodemethod import Explode
from common.getfilemethod import GetFile
from common.itembase import ItemBase
from common.readiniconfig import ReadIniData
from data.datalist import DataList


class Bullet(ItemBase):
    def __init__(self, tank):
        super(Bullet, self).__init__()
        self.getimage = GetFile()
        # 子弹图片
        self.image = pygame.image.load(self.getimage.getimagefile('enemymissile.gif'))
        # 子弹方向
        self.direction = tank.direction
        # 子弹位置/子弹图片的rect
        self.rect = self.image.get_rect()
        if self.direction == "UP":
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == "DOWN":
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + self.rect.height
        elif self.direction == "LEFT":
            self.rect.left = tank.rect.left - self.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        elif self.direction == "RIGHT":
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        # 子弹速度
        self.speed = 7
        # 子弹存在状态
        self.live = True
    # 子弹移动方法
    def bulletmove(self):
        windowsize = ReadIniData()
        if self.direction == "UP":
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.live = False
        elif self.direction == "DOWN":
            if self.rect.bottom < int(windowsize.getwindowsize()[0]):
                self.rect.top += self.speed
            else:
                self.live = False
        elif self.direction == "LEFT":
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.live = False
        elif self.direction == "RIGHT":
            if self.rect.right < int(windowsize.getwindowsize()[1]):
                self.rect.left += self.speed
            else:
                self.live = False
    # 绘制子弹
    def displaybullet(self):
        DataList.window.blit(self.image, self.rect)

    # 玩家子弹碰撞敌人坦克的方法
    def hitenemytank(self):
        for etank in DataList.ENEMYTANK_LIST:
            if pygame.sprite.collide_rect(etank, self):
                # 产生一个爆炸效果
                explode = Explode(etank)
                # # 将爆炸效果加入到爆炸效果列表
                DataList.EXPLODE_LIST.append(explode)
                self.live = False
                etank.live = False
    # 敌方坦克子弹命中玩家的方法
    def hitplayertank(self):
        if pygame.sprite.collide_rect(self, DataList.TANK_P1):
            # 产生爆炸效果，并加入到爆炸效果列表中
            explode = Explode(DataList.TANK_P1)
            # MainGame.Explode_list.append(explode)
            DataList.EXPLODE_LIST.append(explode)
            self.live = False
            DataList.TANK_P1.live = False

    # 子弹与墙壁碰撞
    def hitwall(self):
        for wall in DataList.WALL_LIST:
            if pygame.sprite.collide_rect(wall, self):
                self.live = False
                wall.hp -= 1
                if wall.hp <= 0:
                    wall.live = False


if __name__ == '__main__':
    pass
