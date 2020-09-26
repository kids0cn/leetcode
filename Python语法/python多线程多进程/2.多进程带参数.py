import multiprocessing
import time

'''
# 创建子进程 元祖的方式传递参数
sing_process = multiprocess.Process(target=sing,args=(3,))
# 启动子进程
sing_process.start()

# 字典的方式传递参数

'''

def dance(nums,names):
    for i in range(nums):
        print(names+"跳舞")
        time.sleep(0.5)

def sing(nums,names):
    for i in range(nums):
        print(names+"唱歌")
        time.sleep(0.5)

if __name__ == "__main__":
    print("多进程")
    sing_process = multiprocessing.Process(target=sing,args=(5,"小米"))
    dance_process = multiprocessing.Process(target=dance,kwargs={"names":"小茗","nums":6})


    sing_process.start()
    dance_process.start()