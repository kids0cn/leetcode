
with open('1.txt') as file:
    contents = file.read() # 所有内容都被读取
    print(contents.rstrip()) # 删除行尾空格

# 逐行读取
filename = '1.txt'
with open(filename) as fObject:
    for line in fObject:
        print(line.rstrip()) 


# 将文件中的各行存储在一个列表中
with open(filename) as f :
    lines = f.readlines()
for line in lines:
    print(line.rstrip())

