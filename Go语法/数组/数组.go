package main

import (
	"fmt"
)

func main() {
	// 一维数组
	var arr1 [5]int
	fmt.Println(arr1)

	var arr2 = [5]int{1, 2, 3, 4, 5}
	fmt.Println(arr2)

	var arr3 = []int{2, 4, 6, 8, 10}
	fmt.Println(arr3)

	arr4 := []int{0: 3, 1: 5, 4: 6} //指定插入位置
	fmt.Println(arr4)

	//二维数组
	var arr6 = [3][5]int{{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}}
	arr7 := [][5]int{{1, 2, 3, 4, 5}, {6, 7, 8, 9}}
	fmt.Println(arr6)
	fmt.Println(arr7)

	//数组传递 ： 值传递
	arr8 := [5]int{1, 2, 3, 4, 5}
	modifyArr(arr8) //传递进来修改无效
	fmt.Println(arr8)

	//传地址
	modifyArrPtr(&arr8)
	fmt.Println(arr8)

	//数组赋值 同类型数组
	//arr8 = arr4  [5]int 和 []int 都不行
	arr8 = arr2
	fmt.Println(arr8)

	//Go语言传址的问题
	arr9 := []int{1, 2, 3, 4, 5, 6} //这样自己判断数组长度的
	fmt.Println("修改之前\n", arr9)
	modifyArrArr9(arr9)
	fmt.Println("修改之后\n", arr9)
}

func modifyArr(a [5]int) {
	a[1] = 20
}

func modifyArrPtr(a *[5]int) {
	a[1] = 20
}

func modifyArrArr9(a []int) { //这样传进去的是地址
	a[2] = 50
}
