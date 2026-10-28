func countSubstrings(s string) int {
	count := 0
	n := len(s)
	for center := 0; center < 2 * n - 1; center++ {
		left := center / 2
		right := (center + 1) / 2
		for left >= 0 && right < n && s[left] == s[right] {
			count += 1
			left -= 1
			right += 1
		}
	}

	return count
}
