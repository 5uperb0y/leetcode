class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        occur = {}
        for n in nums:
            if n in occur.keys():
                return(True)
            else:
                occur[n] = n
        return(False)