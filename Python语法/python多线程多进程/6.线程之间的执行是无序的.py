import time
import threading

def task():
    time.sleep(1)
    # current_thread 获取当前的线程对象
    thread = threading.current_thread
    print('n')
    print(threading)

if __name__ == "__main__":
    for i in range(5):
        sub_thread = threading.Thread(target=task)
        sub_thread.start()