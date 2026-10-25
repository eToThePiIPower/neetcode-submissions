func hasDuplicate(nums []int) bool {
    seen := make(map[int] bool)
	for _, value := range nums {
		if seen[value] {
			return true
		} else {
			seen[value] = true
		}
	}
	return false
}