func hasDuplicate(nums []int) bool {
    dict := make(map[int] int)
	for _, value := range nums {
		if _, ok := dict[value]; ok {
			return true
		} else {
			dict[value] = 1
		}
	}
	return false
}