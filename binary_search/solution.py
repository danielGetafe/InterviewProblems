class Solution:
    def search(self, nums: list[int], target: int) -> int:
        nums_len = len(nums)
        end_interval = nums_len - 1
        start_interval = 0
        while start_interval <= end_interval:
            index = int((end_interval - start_interval - 1) / 2) + start_interval
            if nums[index] == target:
                return index
            if target > nums[index]:
                start_interval = index + 1
                continue
            end_interval = index - 1
        return -1
