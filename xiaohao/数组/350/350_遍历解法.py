# 解题思路
'''
对比两个数组的大小，将小的数组作为第一层循环的遍历数组，外循环遍历一次
遍历小的数组，对比大数组中是否存在相同的数组，
若存在，将该值加入nums，从大数组中删除该数（表示使用过），退出本次循环
'''

def intersect(nums1,nums2):
    """
    :type nums1:List[int]
    :type nums2:List[int]
    :rtype List[int]
    """

    if len(nums1)>len(nums2):
        nums1,nums2 = nums2,nums1
    for i in nums1:
        for j in nums2:
            if i == j:
                nums.append(i)
                nums2.remove(i)
                break
    return nums



if __name__ == "__main__":
    #nums1 = [4,9,5,5,4]
    #nums2=[9,4,9,8,4,9,8,4,9]
    nums1 = [1,2,2,1]
    nums2 = [2,2] 
    nums = []
    print(intersect(nums1,nums2))


