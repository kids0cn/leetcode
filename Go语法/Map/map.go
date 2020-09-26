/*
- 所有key必须为同一类型
- 所有value必须为同一类型
*/
package main

import (
	"fmt"
)

//map变量的类型 map[int]string

func main() {
	//先声明，再创建，再赋值
	var p1 map[int]string
	p1 = make(map[int]string)
	p1[1] = "Tom"
	fmt.Println("p1", p1)

	//声明的同时创建
	var p2 map[int]string = map[int]string{}
	p2[1] = "Jacky"
	fmt.Println("p2", p2)

	var p3 map[int]string = make(map[int]string)
	p3[1] = "Micky"
	fmt.Println("p3", p3)

	p4 := map[int]string{}
	p4[1] = "Jerry"
	fmt.Println("p4", p4)

	p5 := make(map[int]string)
	p5[1] = "PDD"
	fmt.Println("p5", p5)

	p6 := map[int]string{
		1: "tom",
		2: "jerry",
	}
	fmt.Println("p6", p6)
	//cap不能用在map
	//fmt.Printf("len(p6)=%d,cap(p6)=%d\n", len(p6), cap(p6))

	/*
		map被创建时，可以指定map的容量，但是不能使用cap
	*/
	m := make(map[int]string, 3)
	m[1] = "lp1"
	m[2] = "lp2"
	m[3] = "lp3"
	m[4] = "lp4"
	m[5] = "lp5"
	fmt.Println("m", m) //正常输出

	//编辑和删除
	person := map[int]string{
		1: "Tom",
		2: "Jerry",
		3: "Atom",
	}
	fmt.Println("data", person)

	delete(person, 2)
	fmt.Println("data", person)

	person[2] = "Jack"
	person[3] = "kevin"
	fmt.Println("data", person)

	person[2] = "这几年玩"
	fmt.Println("data", person)
}
