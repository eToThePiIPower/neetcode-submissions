import "maps"

func isAnagram(s string, t string) bool {
	freqs_s := countFreqs(s)
	freqs_t := countFreqs(t)
	return maps.Equal(freqs_s, freqs_t)
}

func countFreqs(s string) map[rune]int {
	freqs := make(map[rune]int)
	for _, char := range s {
		freqs[char]++
	}
	return freqs
}