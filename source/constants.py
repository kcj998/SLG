'''保存游戏的基本设置，字符串信息'''

# 游戏的标题
ORIGINAL_CAPTION = '战棋游戏'

GRID_X_LEN = 10 # 地图的行数
GRID_Y_LEN = 12 # 地图的列数
REC_SIZE = 50   # 地图每个格子的长度
MAP_WIDTH = GRID_X_LEN * REC_SIZE  # 地图的宽度
MAP_HEIGHT = GRID_Y_LEN * REC_SIZE # 地图的高度

SCREEN_WIDTH = MAP_WIDTH   # 游戏界面的宽度
SCREEN_HEIGHT = MAP_HEIGHT # 游戏界面的高度
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 游戏中使用到的颜色
#                R    G    B
WHITE        = (255, 255, 255)
BLACK        = (  0,   0,   0)
SKY_BLUE     = ( 39, 145, 251)
LIGHTYELLOW  = (247, 238, 214)


# 地图背景颜色类型
BG_EMPTY = 0
BG_ACTIVE = 1

# 地图格子类型
MAP_EMPTY = 0 # 格子是空的
MAP_STONE = 1 # 格子中是石头
MAP_GRASS = 2 # 格子中是草地

# 地图配置文件中的属性
MAP_GRID = 'mapgrid'