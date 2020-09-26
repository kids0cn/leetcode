/*
	动态规划
*/

package main

import "fmt"

func maxProfit(prices []int) int {
	//如果没有第二天，买股票就没意义了
	if len(prices) < 2 {
		return 0
	}

	d := make([][2]int, len(prices)) //创建二维动态数组
	d[0][0] = 0                      //卖出利润
	d[0][1] = -prices[0]             //买入利润

	for i := 1; i < len(prices); i++ {
		d[i][0] = max(d[i-1][0], prices[i]+d[i-1][1]) //卖出利润= 前一天买入利润+今天卖出的利润
		d[i][1] = max(d[i-1][1], d[i-1][0]-prices[i]) //买入利润 = 前一天卖出赚的钱-今天买入
	}
	return max(d[len(prices)-1][0], d[len(prices)-1][1])

}

/*
dp[][0] 卖出获利
dp[][1] 买入获利
*/

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	prices1 := []int{7, 1, 5, 3, 6, 4}
	fmt.Println(prices1, maxProfit(prices1))
	prices2 := []int{1, 2, 3, 4, 5}
	fmt.Println(prices2, maxProfit(prices2))

}
