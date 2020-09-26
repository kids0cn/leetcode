package main

import (
	"fmt"
)

func rotate(nums []int, k int) {
	nums[2] = 30
	reverse(nums) //数组先倒序旋转
	reverse(nums[:k%len(nums)])
	reverse(nums[k%len(nums):])
}

func reverse(arr []int) {
	temp := -1
	for k := 0; k < len(arr)/2; k++ {
		temp = arr[k]
		arr[k] = arr[len(arr)-k-1]
		arr[len(arr)-k-1] = temp
	}

}

func main() {
	k := 0
	test1 := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	test2 := []int{1, 2, 3, 4}
	fmt.Println("初始数组")
	fmt.Println(test1)
	fmt.Println(test2)
	fmt.Printf("输入后移位数:")
	fmt.Scanf("%d", &k)
	rotate(test1, k)
	rotate(test2, k)
	fmt.Println("移动后")
	fmt.Println(test1)
	fmt.Println(test2)

}
