package main

import (
	"fmt"
	"sort"
)

func insert(nums1 []int, nums2 []int) []int {
	ptr1, ptr2, length, k := 0, 0, 0, 0

	//排序
	sort.Ints(nums1)
	sort.Ints(nums2)
	fmt.Println(nums1)
	fmt.Println(nums2)

	if len(nums1) < len(nums2) {
		length = len(nums1)
	} else {
		length = len(nums2)
	}

	nums := make([]int, length)

	for ptr1 < len(nums1) && ptr2 < len(nums2) {
		if nums1[ptr1] == nums2[ptr2] {
			nums[k] = nums1[ptr1]
			ptr1 += 1
			ptr2 += 1
			k += 1
		} else if nums1[ptr1] < nums2[ptr2] {
			ptr1+=1
		} else {
			ptr2+=1
		}
	}
	return nums[:k]
}

func main() {
	nums1 := []int{11, 1, 11, 2, 4, 7, 3, 11, 9, 12, 5, 7, 7, 6}
	nums2 := []int{6, 6, 6, 6, 7, 7, 10, 11, 11}
	fmt.Println(insert(nums1, nums2))

}
