package main

import "fmt"

type Person struct {
	Name string
	Age  int
}

func main() {
	var p1 Person
	p1.Name = "Tom"
	p1.Age = 30
	fmt.Println("p1=", p1)

	p2 := Person{Name: "Burke", Age: 31}
	fmt.Println("p2=", p2)

	//匿名结构体
	p4 := struct {
		Name string
		Age  int
	}{Name: "Jack", Age: 33}
	fmt.Println("p4=", p4)

}
