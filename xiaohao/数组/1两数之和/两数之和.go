package main

import (
	"fmt"
)

func twoNumbaoli(nums []int, target int) []int {
	result := []int{}
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i]+nums[j] == target {
				temp := []int{i, j}
				result = append(result, temp...)
			}
		}
	}
	return result
}

func twoNumMap(nums []int, target int) []int {
	result := []int{}
	m := make(map[int]int)
	for i, k := range nums {
		if value, exist := m[target-k]; exist {
			result = append(result, value) //value是下标
			result = append(result, i)
		}
		m[k] = i
	}
	return result
}

func main() {
	nums := []int{2, 7, 3, 6, 11, 15, 1, 8, 8, 1, 0, 7, 9, 17, 15, 13}
	target := 9
	fmt.Println(twoNumMap(nums, target)) //每个数仅使用一次
	fmt.Println(twoNumbaoli(nums, target))
}
