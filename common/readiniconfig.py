import configparser
import os


class ReadIniData:

    def __init__(self):
        # ini路径获取
        inipathbefore = os.path.dirname(os.getcwd())
        inipath = os.path.join(inipathbefore, 'config\config.ini')
        # 实例化ConfigParser类，用于读取ini文件
        self.iniconfig = configparser.ConfigParser()
        self.iniconfig.read(inipath)

    def getwindowsize(self):
        windowheight = self.iniconfig.get('setwindowsize', 'windowheight')
        windowwidth = self.iniconfig.get('setwindowsize', 'windowwidth')
        windowsize = [windowheight, windowwidth]
        return windowsize

    def getimagepath(self):
        return self.iniconfig.get('path', 'imagepath')


if __name__ == '__main__':
    print(ReadIniData().getwindowsize()[0])
    pass
