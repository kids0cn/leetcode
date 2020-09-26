# 解题思路
"""
利用字典统计nums1和nums2每个元素的个数，
取两个字典相同键的最小值
"""
'''
defaultdict的作用是在于，
当字典里的key不存在但被查找时，
返回的不是keyError而是一个默认值
'''
from collections import defaultdict

'''
这个人的思路很差
明明使用第三方的集合库，还把问题搞得这么复杂
用第三方库取交之后还要在重新遍历每一个字典变量，递减字典键值来添加集合

def intersection(nums1,nums2):
    nums = []
    dict1 = defaultdict(int)
    dict2 = defaultdict(int)
    for i in nums1:
        dict1[i] += 1;
    for i in nums2:
        dict2[i] += 1;
    
    # set是集合，& 则是取交集
    for i in set(dict1)&set(dict2):
        x = min(dict1[i],dict2[i])
        print(x)
        
    return nums
'''

from collections import Counter

def intersection(nums1,nums2):
    num1 = Counter(nums1) # 计数器，直接统计元素变量，个数为键值
    num2 = Counter(nums2)
    nums = num1 & num2
# 这里有问题
    return nums.elements()

if __name__ == "__main__":
    nums1 = [4,9,5,5,4]
    nums2=[9,4,9,8,4,9,8,4,9]
    #nums1 = [1,2,2,1]
    #nums2 = [2,2] 
    print(intersection(nums1,nums2))
