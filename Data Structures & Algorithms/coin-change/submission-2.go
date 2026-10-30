func coinChange(coins []int, amount int) int {
	dp := make(map[int]int)
	dp[0] = 0 // start with the base case
	ans := dfs(amount, coins, dp)
	if ans == math.MaxInt {
		return -1
	} else {
		return ans
	}
}

func dfs(amount int, coins []int, cache map[int] int) int {
	cached, ok := cache[amount]
	if ok { return cached }
	if amount < 0 { return math.MaxInt }
	
	val := math.MaxInt
	for i := 0; i < len(coins); i++ {
		new_val := dfs(amount - coins[i], coins, cache)
		if new_val != math.MaxInt && 1 + new_val < val {
			val = 1 + new_val
		}
	}
	cache[amount] = val
	return val
}