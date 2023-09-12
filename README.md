## Fun with Infinity

This is how you can define -infinity and +infinity in Python:

```py
float('-inf')
float('+inf')
```
Examples of how infinity works in Python
```py
print(float('-inf'))
print(float('-inf') + float('-inf') )
print(float('+inf') * 10)
print(float('-inf') + float('+inf') )
print(1/float('inf'))
print(max(1000, float('-inf')))
```
Output:
```
-inf
-inf
inf
nan
0.0
1000
```
Note that infinity - infinity is undefined in Math.
Python yields this as `nan`(NaN -- Not a Number):

Here is the example how to use -infinity to compute maximum window:

```py
def find_max_window(nums: list[int], k: int) -> float:
    window_max = float('-inf')
    for i in range(len(nums) - k + 1):
        window_k = nums[i:i + k]
        window_sum = sum(window_k)
        window_max = max(window_sum, window_max)
    return window_max 
```

Note that that is 0(n^2)algorithm. 
But there is nore efficient linear in time algorithm.



