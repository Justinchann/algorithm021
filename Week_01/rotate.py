class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        s = k%n
        for i in range(s,n):
            nums[i],nums[(i+k)%n] = nums[(i+k)%n],nums[i]