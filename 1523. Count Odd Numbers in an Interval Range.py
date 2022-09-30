class Solution:
    def countOdds(self, low: int, high: int) -> int:
        m = high - low
        if low % 2 == 0 and high % 2 == 0:
            n = m / 2
        elif low % 2 == 0 or high % 2 == 0:
            n = (m+1) / 2
        elif m == 0:
            if low % 2 == 0:
                n = 0
            else: 
                n = low - (low-1)
        else:
            n = ((m)/2) + 1
        return int(n)