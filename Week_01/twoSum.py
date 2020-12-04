class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 暴力求解，时间复杂度O（n2）
        # res = []
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             res.append(i)
        #             res.append(j)
        #             return res
        # return res

        # 哈希表求解，时间复杂度O（1）
        res = []
        hashmap = dict()
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [hashmap[target - nums[i]], i]
            hashmap[nums[i]] = i