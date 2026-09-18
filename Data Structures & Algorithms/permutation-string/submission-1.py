class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        targ = dict()
        for c in s1:
            targ[c] = targ.get(c, 0) + 1
        
        curr = dict()
        p1, p2 = 0, 0
        while p2 < len(s2):
            c = s2[p2]
            print(f"c: {c}, targ: {targ}, curr: {curr}")
            if c in targ:
                while curr.get(c, 0) >= targ[c]:
                    cp = s2[p1]
                    curr[cp] -= 1
                    p1 += 1
                curr[c] = curr.get(c, 0) + 1
                p2 += 1
                if p2 - p1 == len(s1): return True


            else:
                curr = dict()
                p2 += 1
                p1 = p2
        return False

     