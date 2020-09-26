import time 
import os
import multiprocessing

if __name__ == '__main__':
    source_dir = ".//"
    dest_dir = ".//copy"

    try:
        os.mkdir(dest_dir)
    except:
        print("目标文件夹存在")

    