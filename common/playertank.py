import pygame
from common.tankbase import TankBase
from data.datalist import DataList


class PlayerTank(TankBase):
    def __init__(self, left, top):
        super(PlayerTank, self).__init__(left, top)
    # 主动碰撞敌方坦克
    def collisionenemytank(self):
        """
        主动碰撞敌方坦克后，玩家坦克的动作处理
        :param enemytanks: 敌方坦克列表
        :return:
        """
        for enemytank in DataList.ENEMYTANK_LIST:
            if pygame.sprite.collide_rect(self, enemytank):
                self.stay()


if __name__ == '__main__':
    pass