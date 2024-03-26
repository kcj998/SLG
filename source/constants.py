'''保存游戏的基本设置，字符串信息'''

#标题
ORIGINAL_CAPTION = '战棋游戏'

GRID_X_LEN = 10 #地图行
GRID_Y_LEN = 12 #地图列
REC_SIZE = 50   #地图每个格子的长度
MAP_WIDTH = GRID_X_LEN * REC_SIZE  #地图宽
MAP_HEIGHT = GRID_Y_LEN * REC_SIZE #地图高

SCREEN_WIDTH = MAP_WIDTH   # 游戏宽度
SCREEN_HEIGHT = MAP_HEIGHT # 游戏高度
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 颜色定义RGB
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
SKY_BLUE = (39, 145, 251)
LIGHTYELLOW = (247, 238, 214)


# 地图背景颜色类型
BG_EMPTY = 0
BG_ACTIVE = 1

# 地图格子类型
MAP_EMPTY = 0  #空各自
MAP_STONE = 1  #石头格子
MAP_GRASS = 2  #草地格子

# 地图配置文件中的属性
MAP_GRID = 'mapgrid'