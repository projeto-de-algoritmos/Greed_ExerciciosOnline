class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pont = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= pont:
                pont = i

        return True if pont == 0 else False

        
# dados: accepted com 339 ms, memory 14.50 mb

#    Testes
sol = Solution()
print(sol.canJump([2,3,1,1,4]))
print(sol.canJump([3,2,1,0,4]))