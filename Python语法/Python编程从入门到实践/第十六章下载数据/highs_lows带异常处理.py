import csv
import matplotlib.pyplot as plt 
from datetime import datetime

filename = 'death_valley_2014.csv'

'''
with open(filename) as f:
    reader = csv.reader(f) # 用csv的reader方法处理文件f
    header_row = next(reader) # next 返回迭代器的下一个项目
    
    for index,column_header in enumerate(header_row):
        print(index,column_header)
'''
# 处理数据获取文件中的最高温度,最低温度和日期

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) # 每次都会返回下一个
    dates,highs,lows = [],[],[]
    for row in reader: # 每次调用，都会往下走一行
        try:
            current_data = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_data,'missing date')
        else:
            dates.append(current_data)
            highs.append(high)
            lows.append(low)
    print(highs)


    # 根据数据绘制图形
    fig = plt.figure(dpi=128,figsize=(10,6))
    plt.plot(dates,highs,c='red')
    plt.plot(dates,lows,c='blue')

    #填充两个值之间的空间  dates是x值的列表，后面是两个y
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.5)

    # 设置图形的格式
    plt.title("Daily high temp")
    plt.xlabel('',fontsize=15)
    plt.ylabel("Temp",fontsize=15)
    fig.autofmt_xdate() # 用来自动格式化x轴标签，防止重合
    plt.show()