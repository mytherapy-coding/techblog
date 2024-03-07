
## Fun with Counter

```py
count = collections.Counter(string.lower())
```
---
## Different ways how to check if the number is even

```py
nums[0] == 0
if True ==> 1
if False ==> 0

nums[0] % 2 == 0

nums[0]*(nums[0] % 2 == 0)
if True ==> nums[0]*1 == nums[0]
if False ==> nums[0]*0 == =

sum(num * (1-(num % 2)) for num in nums) same as sum(num * (num % 2 == 0) for num in nums)
sum(filter(lambda x: 1-x%2, nums)) same as sum(filter(lambda x: x%2 == 0, nums)) same as sum(filter(lambda x: 1-x & 1, nums)) same as sum(filter(lam
```

---


