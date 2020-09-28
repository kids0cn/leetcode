import matplotlib.pyplot as plt 

from random_walk import RandomWalk



while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points)) # 顺序列表
    plt.scatter(rw.x_values,rw.y_values,s=1,c=point_numbers,\
        cmap=plt.cm.Blues,edgecolors='none')

    # 突出起点和终点
    plt.scatter(0,0,c='green',edgecolors='none',s=40)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=40)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    #plt.figure(dpi=128,figsize=(10,6))
    plt.savefig("random.png")
    plt.show()

    keeprunning = input("Make another walk?(y/n):")

    if keeprunning == 'n':
        break
