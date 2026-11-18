class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):  # ensures i != j and avoids duplicates
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []





        # for i in nums:
        #     for j in nums:
        #         if(i+j == target):
        #             if(i==j):
        #                 return [nums.index(i), nums.index(j,nums.index(i)+1)]
        #             return [nums.index(i),nums.index(j)]
                    



                # if(i+j == target):
                #     if (i<0 and j<0):
                #         return [nums.index(i),nums.index(j)]
                #     elif(i<j or j<i or i<0 or j<0):
                #         return [nums.index(i),nums.index(j)]
                #     elif(i==j):
                #         return [nums.index(i), nums.index(j,nums.index(i)+1)]
                    
        