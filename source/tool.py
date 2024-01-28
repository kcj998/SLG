import os  # 加载 os 模块
import pygame as pg
from . import constants as c
from . import level

class Control():
    def __init__(self):

        pass

    def update(self):
        pass

    def event_loop(self):
        pass

    def main(self):
        # 程序主循环
        pass

def getImage(sheet, x, y, width, height, colorkey, scale):
    pass

def loadAllGraphics(directory, colorkey=c.WHITE, accept=('.png', '.jpg', '.bmp', '.gif')):
    pass

def getMapGridImage():
    pass

# pygame 的初始化
pg.init()
# 设置游戏窗口的标题
pg.display.set_caption(c.ORIGINAL_CAPTION)
# 设置游戏窗口的大小（宽度和高度）
pg.display.set_mode(c.SCREEN_SIZE)

# 加载 resources/graphics 目录中所有的图片文件
GFX = loadAllGraphics(os.path.join("resources","graphics"))
# 获取地图格子类型的图片
GRID = getMapGridImage()