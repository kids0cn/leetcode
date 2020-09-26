/*
package main
import "fmt"

func intersect(nums1 []int, nums2 []int) []int {
    m0 := map[int]int{}
    for _, v := range nums1 { //_是键，v是值；nums是数组，应该是序号
        //遍历nums1，初始化map
        m0[v] += 1
    }
    k := 0
    for _, v := range nums2 {
        //如果元素相同，将其存入nums2中，并将出现次数减1
        if m0[v] > 0 {
            m0[v] -=1
            nums2[k] = v
            k++
        }
    }
    return nums2[0:k]
}

func main(){
	var nums1 = []int{1,1,2,3,4,5}
	var nums2 = []int{2,3,4}
	fmt.Println(intersect(nums1,nums2))
}

*/