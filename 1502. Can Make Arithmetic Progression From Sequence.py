class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort(reverse = True)
        diff = arr[0] - arr[1]
        valid = 0
        for i in range(len(arr)-1):
            if arr[i] - arr[i+1] == diff:
                pass
            else:
                return False
        return True