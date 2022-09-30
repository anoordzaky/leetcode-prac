class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = [int(i) for i in list(str(n))]
        total = sum(n)
        product = 1
        for i in n:
            product *= i
        return product - total