import matplotlib.pyplot as plt 

x_values = list(range(1,10))
y_values = [x**2 for x in x_values]

#plt.scatter(x_values,y_values,s=40)

# 做一个颜色映射,cmap做颜色隐射，y较小的为浅蓝色，大的为深蓝色
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=40)

plt.title("Title")
plt.xlabel("Value",fontsize=14)
plt.ylabel("Squre of value",fontsize=14)
plt.tick_params(axis='both',labelsize=14)

# 设置每哥坐标轴的取值范围
plt.axis([0,11,0,110])

# 自动保存到文件 要在显示之前保存图片
plt.savefig("squares_plot.png",bbox_inches='tight')

plt.show()
