import pygame as pg
from . import tool
from . import constants as c

class Map():
    def __init__(self, width, height, grid):
        #地图行数
        self.width = width
        #地图列数
        self.height = height
        #二维数组，每个元素对应一个地图格子。
        self.bg_map = [[0 for x in range(self.width)] for y in range(self.height)]
        self.setupMapImage(grid)

    def setupMapImage(self, grid):
        pass

    def isValid(self, map_x, map_y):
        #地图 x 和 y 的值是否是有效
        if (map_x < 0 or map_x >= self.width or
            map_y < 0 or map_y >= self.height):
            return False
        return True

    def getMapIndex(self, x, y):
        #返回坐标所在的格子位置
        return (x//c.REC_SIZE, y//c.REC_SIZE)

    def setMouseClick(self, mouse_pos):
        pass

    def drawBackground(self, surface):
        pass