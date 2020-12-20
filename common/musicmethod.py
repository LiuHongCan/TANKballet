import pygame

from common.getfilemethod import GetFile


class Music():
    def __init__(self, filename):
        self.getfile = GetFile()
        self.filename = filename
        # 初始化混合器
        pygame.mixer.init()
        pygame.mixer.music.load(self.getfile.getimagefile(filename))

    def playmusic(self):
        pygame.mixer.music.play()

if __name__ == '__main__':
    pass
