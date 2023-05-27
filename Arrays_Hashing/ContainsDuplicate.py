class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = set()

        for n in nums:
            res.add(n)

        return len(res) != len(nums)
