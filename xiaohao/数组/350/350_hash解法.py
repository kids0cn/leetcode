# 解题思路
'''
用哈希表纪录元素的个数，与nums2对比时，每次使用，就减少一个
'''

def intersect(nums1,nums2):
    """
    :type nums1:List[int]
    :type nums2:List[int]
    :rtype List[int]
    """
    nums = []
    if len(nums1)>len(nums2):
        nums1,nums2 = nums2,nums1
    # 创建Hash表
    hash = {} # 字典
    for i in nums1:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i] += 1
    
    for j in nums2:
        if j in hash and hash[j] > 0:
            nums.append(j)
            hash[j] -= 1
    
    return nums



if __name__ == "__main__":
    nums1 = [4,9,5,5,4]
    nums2=[9,4,9,8,4,9,8,4,9]
    #nums1 = [1,2,2,1]
    #nums2 = [2,2] 
    print(intersect(nums1,nums2))