package main

import "fmt"

func plusOne(nums []int) []int {
	for i := len(nums) - 1; i >= 0; i-- {
		nums[i] = (nums[i] + 1) % 10
		if nums[i]%10 != 0 {
			return nums
		}
	}
	numsplus := make([]int, 1)
	numsplus[0] = 1
	nums = append(numsplus, nums...)
	return nums
}

func main() {
	nums := []int{1, 2, 3}
	fmt.Println(plusOne(nums))
	nums1 := []int{1, 2, 3, 9, 9}
	fmt.Println(plusOne(nums1))
	nums2 := []int{9, 9, 9}
	fmt.Println(plusOne(nums2))

}
