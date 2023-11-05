class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        
        max_reach = nums[0]
        steps = nums[0]
        jumps = 1
        
        for i in range(1, len(nums)):
            if i == len(nums) - 1:
                return jumps
            
            max_reach = max(max_reach, i + nums[i])
            steps -= 1
            
            if steps == 0:
                jumps += 1
                steps = max_reach - i
        
        return jumps
    

# accepted runtime 89 ms, memory 14.85 mb

#Teste
sol = Solution()
print(sol.jump([2, 3, 1, 1, 4]))  # Saída esperada: 2