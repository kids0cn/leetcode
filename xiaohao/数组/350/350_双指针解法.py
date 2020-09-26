# 排序之后用双指针
'''
两个指针遍历排序好的数组
若是指的元素相同，添加到新的数组
不同
值小的指针后移

'''

def intersect(nums1,nums2):
    """
    :type nums1:List[int]
    :type nums2:List[int]
    :rtype List[int]
    """
    nums1.sort()
    nums2.sort()
    nums = []
    i,j = 0,0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            nums.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return nums



if __name__ == "__main__":
    #nums1 = [4,9,5,5,4]
    #nums2=[9,4,9,8,4,9,8,4,9]
    nums1 = [1,2,2,1]
    nums2 = [2,2] 
    print(intersect(nums1,nums2))