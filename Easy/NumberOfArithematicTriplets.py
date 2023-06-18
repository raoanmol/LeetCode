class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        tally = set()
        count = 0
        for i in nums:
            if i - diff in tally and i - diff * 2 in tally:
                count += 1
            tally.add(i)
        return count
