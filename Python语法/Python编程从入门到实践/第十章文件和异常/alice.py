filename = 'Alice.txt'

# except-else 

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    '''
    msg = "Sorry,the file "+filename+" does not exist"
    print(msg)
    '''
    pass # 发现异常不采取任何操作
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The fiel"+filename+" has about "+ str(num_words)+" words.")

