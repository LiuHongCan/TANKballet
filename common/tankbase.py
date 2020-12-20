from common.bullet import Bullet
from common.getfilemethod import GetFile
from common.itembase import ItemBase
import pygame
from common.readiniconfig import ReadIniData
from data.datalist import DataList


class TankBase(ItemBase):
    def __init__(self, left, top):
        # 实例化获取文件绝对路径的类
        self.getimage = GetFile()
        super().__init__()
        # 获取坦克的图片/加载
        self.images = {
            "UP": pygame.image.load(self.getimage.getimagefile('p1tankU.gif')),
            "DOWN": pygame.image.load(self.getimage.getimagefile('p1tankD.gif')),
            "LEFT": pygame.image.load(self.getimage.getimagefile('p1tankL.gif')),
            "RIGHT": pygame.image.load(self.getimage.getimagefile('p1tankR.gif'))
            }
        # 设置初始方向的图片
        self.direction = "UP"
        self.image = self.images[self.direction]
        # 获取坦克图片的rect大小
        self.rect = self.image.get_rect()
        # 指定坦克图片的初始位置
        self.rect.left = left
        self.rect.top = top
        # 设置默认速度
        self.speed = 5
        # 坦克移动开关,默认关
        self.stop = True
        # 坦克live 标记坦克是否存活
        self.live = True
        # TANK之前的位置坐标，用于坐标还原
        self.oldleft = self.rect.left
        self.oldtop = self.rect.top

    # tank移动方法
    def tankmove(self):
        # 先记录移动之前的坐标
        self.oldleft = self.rect.left
        self.oldtop = self.rect.top
        if self.direction == 'LEFT':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'RIGHT':
            # 可能有问题
            if self.rect.right < int(ReadIniData().getwindowsize()[1]):
                self.rect.left += self.speed
        elif self.direction == 'UP':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'DOWN':
            if self.rect.bottom < int(ReadIniData().getwindowsize()[0]):
                self.rect.top += self.speed

    def stay(self):
        self.rect.top = self.oldtop
        self.rect.left = self.oldleft

    # 碰撞墙壁的处理
    # 改进，墙壁变为一个类，只要碰撞到这个类（有碰撞设定开启）就执行碰撞处理
    # walls 表示墙壁列表
    def hitwalls(self):
        for wall in DataList.WALL_LIST:
            if pygame.sprite.collide_rect(wall, self):
                self.stay()
    # 射击方法
    def shot(self):
        return Bullet(self)

    # 绘制坦克,window 表示主窗口
    def dispalytank(self):
        #1.重新设置图片
        self.image = self.images[self.direction]
        # print(self.image)
        #2.将坦克绘制到窗口中
        DataList.window.blit(self.image, self.rect)

if __name__ == '__main__':
    print(TankBase(100,100).dispalytank())
    pass
