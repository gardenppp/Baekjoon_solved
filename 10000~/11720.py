n=int(input())
nums = list(input())
sum = 0
for i in range(n):
    nums[i] = int(nums[i])
    sum+=nums[i]
print(sum)