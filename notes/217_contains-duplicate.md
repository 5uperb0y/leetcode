217. Contains Duplicate
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

Example:

```
Input: nums = [1,2,3,1]
Output: true
```
## 解題思路

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        occur = {}
        for n in nums:
            if n in occur.keys():
                return(True)
            else:
                occur[n] = n
        return(False)
```

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return(True)
        else:
            return(False)
```

## 討論

### 1. set()

### 2. hash, dict, set
