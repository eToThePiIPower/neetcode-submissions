func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	var freqs [26]int
	var zeroes [26]int

	for i := range(s) {
		freqs[s[i] - 'a']++
		freqs[t[i] - 'a']--
	}

	return freqs == zeroes
}