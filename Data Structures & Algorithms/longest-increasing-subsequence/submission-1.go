import "slices"

func lengthOfLIS(nums []int) int {
    n := len(nums)
	dp := make([]int, n) // dp[i] is length of largest subsequence ending at i, minus 1

	for i := 1; i < n; i++ {
		for j := 0; j < i; j++ {
			if nums[j] < nums[i] {
				dp[i] = max(dp[i], dp[j] + 1)
			}
		}
	}

	return slices.Max(dp) + 1
}