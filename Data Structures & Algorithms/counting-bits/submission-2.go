func countBits(n int) []int {
	dp := make([]int, n+1)
	offset := 1
	for i := 1; i <= n; i++ {
		if i == offset * 2 {
			dp[i] = 1
			offset = i
		} else {
			dp[i] = dp[i - offset] + 1
		}
	}

	return dp
}
