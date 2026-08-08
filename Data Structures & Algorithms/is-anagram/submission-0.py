class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = self.__count_freq(s)
        freq_t = self.__count_freq(t)
        return freq_s == freq_t

    def __count_freq(self, s: str) -> dict:
        freq = {}
        for l in s:
            if l not in freq:
                freq[l] = 1
            else:
                freq[l] += 1
        return freq