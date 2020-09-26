import multiprocessing
import time
import os


'''
import os
print("work进程编号",os.getpid())
'''

def dance(nums,names):
    print("dance进程id:"+str(os.getpid()))
    print("dance父进程id:"+str(os.getppid()))
    for i in range(nums):
        print(names+"跳舞")
        time.sleep(0.5)

def sing(nums,names):
    print("sing进程id:"+str(os.getpid()))
    print("sing进程父id:"+str(os.getppid()))
    for i in range(nums):
        print(names+"唱歌")
        time.sleep(0.5)

if __name__ == "__main__":
    print("多进程")
    sing_process = multiprocessing.Process(target=sing,args=(5,"小米"))
    dance_process = multiprocessing.Process(target=dance,kwargs={"names":"小茗","nums":6})

    print("主进程id:"+str(os.getpid()))
    sing_process.start()
    dance_process.start()