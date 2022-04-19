class Solution(object):
    def countBits(self, n):
        
        #M-1
        
        dp=[0]* (n+1)
        
        for i in range(1,n+1):
            if i%2==1:
                dp[i]=(dp[i-1]+1)
            else:
                dp[i]= dp[i//2]
        return dp
        
        
        #M-2
        # return [bin(i)[2:].count("1") for i in range(0,n+1)]
        
        #M-3
        
#         dp=[0]*(n+1)
        
#         for i in range(1,n+1):
#             dp[i]=(dp[i>>1]+i%2)
#         return dp
        
        """
        :type n: int
        :rtype: List[int]
        """
        
