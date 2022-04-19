class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum=[]
        a=0
        for i in nums:
            a+=i
            self.sum.append(a)        
            

    def sumRange(self, left, right):
        if right>0 and left>0:
            return self.sum[right]-self.sum[left-1]
        else:
            return self.sum[right]
        
        
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
