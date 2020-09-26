package main

import "fmt"

/*
Go语言中 cap和len的区别
len是当前数组的长度
cap是申请了动态数组的全部长度,cap是容量

*/

func main() {
	var sli1 []int //null切片
	fmt.Printf("Len=%d Cap=%d Slice=%v\n", len(sli1), cap(sli1), sli1)

	var sli2 = []int{} //空切片
	fmt.Printf("Len=%d Cap=%d Slice=%v\n", len(sli2), cap(sli2), sli2)

	var sli3 = []int{1, 2, 3, 4, 5}
	fmt.Printf("Len=%d Cap=%d Slice=%v\n", len(sli3), cap(sli3), sli3)

	var sli4 []int = make([]int, 5, 8)
	fmt.Printf("Len=%d Cap=%d Slice=%v\n", len(sli4), cap(sli4), sli4)

	sli5 := make([]int, 5, 19)
	fmt.Printf("Len=%d Cap=%d Slice=%v\n", len(sli5), cap(sli5), sli5)

	//切片练习
	slic := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Printf("len=%d,cap=%d,slice=%v\n", len(slic), cap(slic), slic)

	fmt.Println("sli[1] ==", slic[1])
	fmt.Println("slic[:] == ", slic[:])
	fmt.Println("slic[2:] == ", slic[2:])
	fmt.Println("slic[:4] == ", slic[:4]) //不包含4

	fmt.Println("slic[0:3] == ", slic[0:3])
	fmt.Printf("len=%d,cap=%d,slice=%v\n", len(slic[0:3]), cap(slic[0:3]), slic[0:3])

	//用切片创建新的切片
	//实际上是创建了一个容量为4的新切片，内容为0:3
	fmt.Println("slic[0:3:4] == ", slic[0:3:4])
	fmt.Printf("len=%d,cap=%d,slice=%v\nj", len(slic[0:3:4]), cap(slic[0:3:4]), slic[0:3:4])

	// 追加切片
	// 容量不够时，会使容量翻倍，直到下次不够的时候
	slic1 := []int{4, 5, 6}
	fmt.Printf("len=%d,cap=%d,slic1=%v\n", len(slic1), cap(slic1), slic1)

	slic1 = append(slic1, 1)
	fmt.Printf("len=%d,cap=%d,slic1=%v\n", len(slic1), cap(slic1), slic1)

	slic1 = append(slic1, 1)
	fmt.Printf("len=%d,cap=%d,slic1=%v\n", len(slic1), cap(slic1), slic1)

	slic1 = append(slic1, 1)
	fmt.Printf("len=%d,cap=%d,slic1=%v\n", len(slic1), cap(slic1), slic1)

	slic1 = append(slic1, 2) //注意看此时容量翻倍
	fmt.Printf("len=%d,cap=%d,slic1=%v\n", len(slic1), cap(slic1), slic1)

	//删除切片
	slic2 := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Printf("len=%d,cap=%d,slic2=%v\n", len(slic2), cap(slic2), slic2)

	//删除尾部两个元素
	slic2 = slic2[:len(slic2)-2]
	fmt.Printf("len=%d,cap=%d,slic2=%v\n", len(slic2), cap(slic2), slic2)

	//删除开头两个元素
	slic2 = slic2[2:]
	fmt.Printf("len=%d,cap=%d,slic2=%v\n", len(slic2), cap(slic2), slic2)

	//删除中间两个元素
	slic2 = append(slic2[:3], slic2[3+2:]...)
	fmt.Printf("len=%d,cap=%d,slic2=%v\n", len(slic2), cap(slic2), slic2)
}
