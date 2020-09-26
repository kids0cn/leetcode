import multiprocessing
import time

'''
# 创建子进程
sing_process = multiprocess.Process(target=sing)
# 启动子进程
sing_process.start()
'''

def dance():
    for i in range(3):
        print("跳舞")
        time.sleep(0.5)

def sing():
    for i in range(3):
        print("唱歌")
        time.sleep(0.5)

if __name__ == "__main__":
    print("单进程顺序执行")
    sing()
    dance()
    print("多进程")
    sing_process = multiprocessing.Process(target=sing)
    dance_process = multiprocessing.Process(target=dance)

    sing_process.start()
    dance_process.start()