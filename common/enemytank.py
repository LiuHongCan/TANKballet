import random
import pygame
from common.bullet import Bullet
from common.getfilemethod import GetFile
from common.tankbase import TankBase


class EnemyTank(TankBase):
    def __init__(self, left, top, speed):
        super(EnemyTank, self).__init__(left, top)
        # 实例化获取文件绝对路径的类
        self.getimage = GetFile()
        self.images = {
            "UP": pygame.image.load(self.getimage.getimagefile('enemy1U.gif')),
            "DOWN": pygame.image.load(self.getimage.getimagefile('enemy1D.gif')),
            "LEFT": pygame.image.load(self.getimage.getimagefile('enemy1L.gif')),
            "RIGHT": pygame.image.load(self.getimage.getimagefile('enemy1R.gif'))
        }
        self.direction = self.randdirection()
        self.images = self.images[self.direction]
        # 坦克所在区域/坦克图片的大小
        self.rect = self.image.get_rect()
        # 指定坦克初始位置坐标
        self.rect.left = left
        self.rect.top = top

        # 敌方坦克速度
        self.speed = speed
        self.stop = True

        # step属性，控制敌方坦克随机移动
        self.step = 30

    # 随机方向
    def randdirection(self):
        randdirection = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        return randdirection
    # 随机移动
    def randmove(self):
        if self.step <= 0:
            self.direction = self.randdirection()
            self.step = 50
        else:
            self.tankmove()
            self.step -= 1
    # 敌方坦克射击方法
    def shot(self):
        num = random.randint(1, 1000)
        if num <= 20:
            return Bullet(self)
    # 碰到玩家坦克的处理方法
    def collisionplayertank(self, playertank):
        if playertank and playertank.live:
            if pygame.sprite.collide_rect(self, playertank):
                # 敌方坦克停止
                self.stay()


if __name__ == '__main__':
    print(EnemyTank(80, 80, 80).randdirection())
    pass
