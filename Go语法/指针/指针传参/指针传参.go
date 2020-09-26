package main

import "fmt"

func main() {
	//定义局部变量
	var a int = 100
	var b int = 200

	fmt.Printf("交换前两者的值\n a = %d,b = %d\n", a, b)
	swap(&a, &b) //传址交换
	fmt.Printf("交换后两者的值\n a = %d,b = %d\n", a, b)
}

func swap(x *int, y *int) {
	//直接交换地址
	*x, *y = *y, *x
}
