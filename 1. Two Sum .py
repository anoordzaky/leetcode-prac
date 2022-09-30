class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        index_map = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in index_map:
                result.append(i)
                result.append(index_map[diff])
                break
            else:
                index_map[n] = i
        return result