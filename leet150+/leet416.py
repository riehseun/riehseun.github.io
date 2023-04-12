class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 != 0:
            return False

        n = len(nums)
        m = sum(nums) // 2
        
        # [1,2,5,2]
        # dp[i][j] = True if we can pick numbers from nums[:i+1] whose sum equals to the value at j. 
        # dp[i][j] = True means whether dp[i-1][j] is already true or dp[i-1][j-nums[i]] is true 

        #     1 2 5 2  
        #   T F F F F
        # 1 F
        # 2 F
        # 3 F         
        # 4 F
        # 5 F

        dp = []
        for i in range(n+1):
            dp.append([])
            for j in range(m+1):
                dp[i].append(False)
        dp[0][0] = True

        for i in range(1,n+1): 
            for j in range(1,m+1):
                dp[i][j] = dp[i-1][j] or (j >= nums[i-1] and dp[i-1][j-nums[i-1]])

        # for i in range(n+1):
        #     for j in range(m+1):
        #         print(dp[i][j])

        return dp[n][m]      