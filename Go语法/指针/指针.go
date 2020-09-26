package main

/*指针
var var_name *var_type
var ip *int
*/
import (
	"fmt"
)

func main() {
	var a int = 10
	fmt.Printf("变量的地址：%x\n", &a)

	var b int = 20
	var ip *int
	ip = &b
	fmt.Printf("b的内存地址是:%x\n", &b)
	fmt.Printf("ip存储的内容是:%x\n", ip)

	//空指针和空指针判断
	var ptr *int
	fmt.Printf("ptr的值是%x\n", ptr)
	if ptr == nil {
		fmt.Println("True")
	}
}
