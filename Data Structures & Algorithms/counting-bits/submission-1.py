class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        hashMap = {}

        for i in range(n + 1):
            count = 0
            while i:
                if i in hashMap:
                    count += hashMap[i]
                    break
                i &= (i - 1)
                count += 1
            res.append(count)
            hashMap[i] = count
        return res