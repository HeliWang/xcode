import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums_init = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums_init

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nums = list(self.nums_init)
        for i in range(len(nums))[::-1]:
            # swap arbitrary element before i (or i itself) and i
            j = random.randrange(i + 1)
            origin  = nums[j]
            nums[j] = nums[i]
            nums[i] = origin
        return nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()