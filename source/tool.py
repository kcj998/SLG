import os
import pygame as pg
from . import constants as c
from . import level

class Control():
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.done = Falseimport os
import pygame as pg
from . import constants as c
from . import level

class Control():
    def __init__(self):     #游戏基本设定
        self.screen = pg.display.get_surface()
        self.done = False
        self.clock = pg.time.Clock()
        self.fps = 60
        self.level = level.level()
        self.mouse_pos = None

    def update(self):  #更新函数
        self.current_time = pg.time_get_ticks()
        self.level.update(self.screen, self.current_time, self.mouse_pos)
        selfe.mouse.pos = None

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:   #退出游戏
                self.done = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.mouse_pos = pg.mouse.get_pos()

    def main(self):
        while not self.done:
            self.event_loop()
            self.update()
            pg.display.update()
            self.clock.tick(self.fps)

def getImage(sheet, x, y, width, height, colorkey, scale):
    image = pg.Surface([width, height])
    rect = image.get_rect()
    image.blit(sheet,(0,0),(x,y,width,height))
    image.set_colorkey(colorkey)
    image = pg.transform.scale(image,(int(rect.width*scale),int(rect.height*scale)))
    return image

def loadAllGraphics(directory, colorkey=c.WHITE, accept=('.png', '.jpg', '.bmp', '.gif')):
    graphics = {}
    for pic in os.listdir(directory):
        name,ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory,pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img
    return  graphics

def getMapGridImage():
    grid_images = {}
    image_rect_dict = {c.MAP_STONE:(0,16,16,16),c.MAP_GRASS:(0,0,16,16)}
    for type, rect in image_rect_dict():
        grid_images[type] = getImage(GFX['tile'].*rect, c.WHITE,3)
    return  grid_images


pg.init()
#设置游戏标题
pg.display.set_caption(c.ORIGINAL_CAPTION)
#设置游戏窗口的大小（宽度和高度）
pg.display.set_mode(c.SCREEN_SIZE)
#加载 resources/graphics 目录中所有的图片文件(暂无)
GFX = loadAllGraphics(os.path.join("resources","graphics"))
#获取地图格子类型的图片(暂无)
GRID = getMapGridImage()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.level = level.level()
        self.mouse_pos = None

    def update(self):
        self.current_time = pg.time_get_ticks()
        self.level.update(self.screen, self.current_time, self.mouse_pos)
        self.mouse.pos = None

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.mouse_pos = pg.mouse.get_pos()

    def main(self):
        while not self.done:
            self.event_loop()
            self.update()
            pg.display.update()
            self.clock.tick(self.fps)

def getImage(sheet, x, y, width, height, colorkey, scale):
    image = pg.Surface([width, height])
    rect = image.get_rect()
    image.blit(sheet,(0,0),(x,y,width,height))
    image.set_colorkey(colorkey)
    image = pg.transform.scale(image,(int(rect.width*scale),int(rect.height*scale)))
    return image

def loadAllGraphics(directory, colorkey=c.WHITE, accept=('.png', '.jpg', '.bmp', '.gif')):
    graphics = {}
    for pic in os.listdir(directory):
        name,ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory,pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img
    return  graphics

def getMapGridImage():
    grid_images = {}
    image_rect_dict = {c.MAP_STONE:(0,16,16,16),c.MAP_GRASS:(0,0,16,16)}
    for type, rect in image_rect_dict.items():
        grid_images[type] = getImage(GFX['tile'],*rect, c.WHITE,3)
    return  grid_images


pg.init()
#设置游戏标题
pg.display.set_caption(c.ORIGINAL_CAPTION)
#设置游戏窗口的大小（宽度和高度）
pg.display.set_mode(c.SCREEN_SIZE)
#加载 resources/graphics 目录中所有的图片文件(暂无)
GFX = loadAllGraphics(os.path.join("resources","graphics"))
#获取地图格子类型的图片(暂无)
GRID = getMapGridImage()