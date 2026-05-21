class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        zero_cnt=0
        for index_i,value_i in enumerate(nums):
            if value_i:
                product=product*value_i
            else:
                zero_cnt+=1
        if zero_cnt>1: return [0]*len(nums)
        output=[0]*len(nums) 
        for index,c in enumerate(nums):
            if zero_cnt:
                if c==0:
                    output[index]=product
                else:
                    output[index]=0
            else:
                output[index]=product//c
        return output