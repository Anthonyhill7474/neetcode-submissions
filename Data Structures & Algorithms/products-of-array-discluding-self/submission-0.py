class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list1 = [1] * len(nums)
        list2 = [1] * len(nums)

        for i in range(1, len(nums)):
            list1[i] *= nums[i-1]
            list1[i] *= list1[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            list2[i] *= nums[i+1]
            list2[i] *= list2[i+1]

            list1[i] *= list2[i]
        return list1