import pygame
from common.getfilemethod import GetFile


class Wall():
    def __init__(self, left, top):
        getfile = GetFile()
        self.image = pygame.image.load(getfile.getimagefile('steels.gif'))
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        # 墙壁的显示/生成状态
        self.live = True
        # 墙壁的生命值属性
        self.hp = 3
    # 生成墙壁的方法
    def displaywall(self, window):
        window.blit(self.image, self.rect)

if __name__ == '__main__':
    pass
