package main

import (
	"fmt"
	"strings"
)

func longPrefix(str []string) string {
	fmt.Println(str)
	if len(str) < 1 {
		fmt.Println("Error")
		return ""
	}

	prefix := str[0]

	for _, k := range str {
		for strings.Index(k, prefix) != 0 { //在k里找prefix
			if len(prefix) == 0 {
				fmt.Println("Can't find")
				return ""
			}
			prefix = prefix[:len(prefix)-1]
		}
	}

	return prefix
}

func main() {
	string0 := []string{"flower", "flow", "floght"}
	fmt.Println(longPrefix(string0))
}
