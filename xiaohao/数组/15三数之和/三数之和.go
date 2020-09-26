package main

import (
	"fmt"
	"sort"
)

func threeSum(nums []int) [][]int {
	res := [][]int{}
	length := len(nums)
	left := -1
	right := -1
	sum := 0
	// 不够三个直接返回，边界判断
	if length < 3 {
		return res
	}
	sort.Ints(nums)
	for i := 0; i < length; i++ {
		if nums[i] > 0 {
			return res
		}
		left = i + 1
		right = length - 1
		for left < right {
			sum = nums[i] + nums[left] + nums[right]
			if sum > 0 {
				right--
			} else if sum < 0 {
				left++
			} else {
				res = append(res, []int{nums[i], nums[left], nums[right]})
			}
		}
	}
	return res

}

func main() {
	nums := []int{-1, 0, 1, 2, -1, -4}
	fmt.Println(threeSum(nums))
}
