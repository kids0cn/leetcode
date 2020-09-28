from itertools import gropuby # 对数据进行分组并且进行组内计算的包

def draw_line(x_data,y_data,title,y_legend):
    xy_map = []
    for x,y in gropuby(sorted(zip(x_data,y_data)))