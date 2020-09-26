/*
package main

import "fmt"

func intersect(nums1 []int, nums2 []int) []int {
	length := 0
	if len(nums1) > len(nums2) {
		length = len(nums1)
	} else {
		length = len(nums2)
	}

	nums := make([]int, length)
	map0 := map[int]int{}

	for _, i := range nums1 {
		map0[i] += 1

	}
	k := 0
	for _, i := range nums2 {
		if map0[i] > 0 {
			map0[i] -= 1
			nums[k] = i
			k++
		}
	}
	return nums[0:k]
}

func main() {

	nums1 := []int{1, 2, 2, 3, 4, 7}
	nums2 := []int{2, 2, 6, 7, 9}
	fmt.Println(intersect(nums1, nums2))

}
*/