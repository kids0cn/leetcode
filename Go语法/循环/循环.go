package main

import (
	"fmt"
)

func main() {
	person := [3]string{"Tom", "Atom", "John"}
	fmt.Printf("len=%d,cap=%d,array=%v\n", len(person), cap(person), person)

}
