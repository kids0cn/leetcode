package main

import (
	"fmt"
)

const MAX int = 3

func main() {
	a := []int{10, 100, 200}
	var i int

	for i = 0; i < MAX; i++ {
		fmt.Printf("a[%d] = %d\n", i, a[i])
	}

	//数组的声明，[]表示数组及其大小，后面跟的*int则是数组中每个元素的类型
	var ptr [MAX]*int //指针数组，是数组中保存的都是指针
	for i = 0; i < MAX; i++ {
		ptr[i] = &a[i]
	}

	for i = 0; i < MAX; i++ {
		fmt.Printf("a[%d] = %d\n", i, *ptr[i])
	}

}
