package main

import (
	"fmt"
)

func doublePtr(nums []int, val int) []int {
	/*
		双指针的问题，就在于，返回时没有问题的，但是并没有改变数组
		数组后面会带很多冗余
	*/
	i := 0
	for j := 0; j < len(nums); j++ {
		if nums[j] != val {
			nums[i] = nums[j] //我可以通过下表改值，但是却不能通过名字修改值
			i++
		}
	}
	return nums[:i]
}

//利用切片，做就地重组数组
func slice(nums []int, val int) []int {
	for i := 0; i < len(nums); {
		if nums[i] == val {
			nums = append(nums[:i], nums[i+1:]...)
			fmt.Println(nums)
		} else {
			i++
		}
	}
	return nums
}

func main() {
	nums := []int{1, 3, 3, 4, 5, 6, 4, 3, 2, 4, 7}
	fmt.Println(doublePtr(nums, 3))
	fmt.Println(nums)
	fmt.Println("切片法")
	fmt.Println(slice(nums, 3))

}
