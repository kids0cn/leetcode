import matplotlib.pyplot as plt
input_values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
squares = [1,4,9,16,25,36,49,64,81,100,121,144,169]

plt.title("Title",fontsize=24)

plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis='both',labelsize=14)


plt.plot(input_values,squares,linewidth=5)
plt.show()