
from urllib.request import urlopen
import json
'''
json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'

response = urlopen(json_url)

# 读取数据
req = response.read()

# 写入文件
with open('btc_close_2017.json','wb') as f:
    f.write(req)

# 加载json格式
file_urllib = json.loads(req)
print(file_urllib)
'''

# 下载之后处理数据
filename = 'btc_close_2017.json'

with open(filename) as f:
    btc_data = json.load(f) #列表，每个元素是一个五个键值对的字典

print(btc_data[0])
# 打印每一天的信息
for btc_dict in btc_data:
    date = btc_dict['date']
    month = int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close = int(float(btc_dict['close'])) # 带小数点的str不能直接转int
    print("{}is {} month {} week {},the close price is {} RMB".\
        format(date,month,week,weekday,close))

# 绘制图形
dates = []
months = []
weeks = []
weekdays = []
closes = []
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(btc_dict['month'])
    weeks.append(btc_dict['week'])
    weekdays.append(btc_dict['weekday'])
    closes.append(int(float(btc_dict['close'])))

# 对收盘价做半对数处理，消除非线性趋势
import math
close_log = [math.log10(_) for _ in closes]

import pygal 
line_chart = pygal.Line(x_label_rotation = 20,show_minor_x_labels=False) 
# 第一个参数让x轴顺时针旋转20度，第二个参数是说不要显示所有的x
line_chart.title = '收盘价'
line_chart.x_labesls = dates
N = 20 # x坐标轴每隔20天显示一次
line_chart.x_labels_major = dates[::N]
#line_chart.add('收盘价',closes)
line_chart.add("log收盘价",close_log)
#line_chart.render_to_file("收盘价.svg")
line_chart.render_to_file("对数收盘价.svg")