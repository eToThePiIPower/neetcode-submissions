class Solution:

    def encode(self, strs: List[str]) -> str:
        with_len = list(map(lambda s: f"{len(s)}:{s}", strs))
        return "".join(with_len)
    def decode(self, s: str) -> List[str]:
        i = 0
        dec = []
        while i < len(s):
            j = i
            while s[j] != ":":
                j+=1
            length = int(s[i:j])
            dec.append(s[(j+1):(j+1+length)])
            i = j+1+length
        return dec
