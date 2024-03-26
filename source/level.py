import os
import json
import pygame as pg
from . import tool
from . import constants as c
from . import map

class Level():
    def __init__(self):
        self.loadMap()  #读取地图设置
        grid = self.map_data[c.MAP_GRID] if c.MAP_GRID in self.map_data else None
        self.map = map.Map(c.GRID_X_LEN, c.GRID_Y_LEN, grid)               #创建地图类

    def loadMap(self):     #读取地图配置文件 level_x.json
        map_file = 'level_1.json'
        file_path = os.path.join('data', 'map', map_file)
        f = open(file_path)
        self.map_data = json.load(f)
        f.close()

    def GGGGGGGa