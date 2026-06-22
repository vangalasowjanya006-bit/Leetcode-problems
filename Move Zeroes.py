class Solution(object):
    def moveZeroes(self, nums):
        s = []

        for i in nums:
            if i != 0:
                s.append(i)

        for j in nums:
            if j == 0:
                s.append(j)

        for i in range(len(nums)):
            nums[i] = s[i]
