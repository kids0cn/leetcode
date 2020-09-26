def binary_search(lists,elem):
    low,high = 0,len(lists)-1
    #print(low,high)
    while low<high:
       # print("low,high",low,high)
        mid = (low+high)//2
        #print("mid:",mid)
        if lists[mid] == elem:
            return mid
        if lists[mid] > elem:
            high = mid
        else:
            low = mid
    return None
my_lists = [1,3,5,7,9]

print(binary_search(my_lists,3))
print(binary_search(my_lists,-1))
