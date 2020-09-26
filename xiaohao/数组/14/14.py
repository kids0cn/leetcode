
def longPrefix(strTest):
    if len(strTest) < 1:
        print("error")
        return ""
    prefix = strTest[0]
    for i in strTest:
        if len(prefix) == 0:
            print("cant't find")
            return ''
        while i.find(prefix) != 0: # 只有当前设定的prefix不是前缀，才进入循环
            prefix = prefix[:-1]
            print(i,prefix)
        '''
        这样的问题是，flow,owfl 结果都是true，不能判断是前缀
        需要使用find方法，find可以返回子字符串出现的位置，为0就是前缀
        if prefix not in i:
            prefix = prefix[:-1]
        '''    
    return prefix


if __name__ == '__main__':
    str0 = ["china","change","choke","chance","child"]
    print(longPrefix(str0))

