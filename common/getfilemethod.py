from common.readiniconfig import ReadIniData
import os

class GetFile:
    def __init__(self):
        self.beforepath = os.path.dirname(os.getcwd())

    def getimagefile(self, filename):
        filepath = os.path.join(self.beforepath, ReadIniData().getimagepath())
        iamgefile = filepath + filename
        return iamgefile
if __name__ == '__main__':
    print(GetFile().getimagefile('enemymissile.gif'))
    pass