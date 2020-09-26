import time
import threading

'''
# 创建子线程
sing_thread = threading.ThreaD(target=sing)
# 启动子进程
sing_thread.start()
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
    print("单线程顺序执行")
    sing()
    dance()
    print("多线程")
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)

    sing_thread.start()
    dance_thread.start()