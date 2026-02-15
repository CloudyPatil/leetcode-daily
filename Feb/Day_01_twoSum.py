class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashMap = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in HashMap:
                return[HashMap[difference], i]
            HashMap[n] = i
        return        