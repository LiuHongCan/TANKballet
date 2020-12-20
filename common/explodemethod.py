import pygame
from common.getfilemethod import GetFile
from data.datalist import DataList


class Explode():
    def __init__(self, tank):
        self.rect = tank.rect
        self.step = 0
        getfile = GetFile()
        self.images = [
                        pygame.image.load(getfile.getimagefile('blast0.gif')),
                        pygame.image.load(getfile.getimagefile('blast1.gif')),
                        pygame.image.load(getfile.getimagefile('blast2.gif')),
                        pygame.image.load(getfile.getimagefile('blast3.gif')),
                        pygame.image.load(getfile.getimagefile('blast4.gif'))
                       ]
        self.image = self.images[self.step]
        self.live = True
    # 展示爆炸效果
    def displayexplode(self):
        if self.step < len(self.images):
            DataList.window.blit(self.image, self.rect)
            self.image = self.images[self.step]
            self.step += 1
        else:
            self.live = False
            self.step = 0
if __name__ == '__main__':
    pass
