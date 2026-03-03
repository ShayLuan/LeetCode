class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        for i, n in enumerate(nums):
            diff = target - n

            # check if diff is in the dict
            if diff in prev_map:
                return [prev_map[diff], i]
            
            # if not found, store the current number and its index
            prev_map[n] = i
        return []