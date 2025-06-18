'''You’re given:
nums = [4, 9, 13, 18, 7, 2, 15, 20]
Your task:
If the number is divisible by 3, multiply it by 5
If it’s even but not divisible by 3, divide it by 2
If it’s odd and not divisible by 3, add 7
Store all results in a new list
From that new list, create another list with values that are between 10 and 50 (inclusive)
Print both lists'''

nums = [4, 9, 13, 18, 7, 2, 15, 20]
mod_nums = []
values = []

for i in range(len(nums)):
    if nums[i] % 3 == 0:
        nums[i] *= 5
        mod_nums.append(nums[i])
    elif nums[i] % 2 == 0 and nums[i] % 3 != 0:
        nums[i] //= 2
        mod_nums.append(nums[i])
    elif nums[i] % 2 == 1 and nums[i] % 3 != 0:
        nums[i] += 7
        mod_nums.append(nums[i])
        
for i in range(len(mod_nums)):
    if 10 <= mod_nums[i] <= 50:
        values.append(mod_nums[i])        
        
        
print(f"In this exercise, we got a given list {nums}, and modified it to meet certain conditions given to us.")
print(f"Our first modified list: {mod_nums}")
print(f"Our second modified list: {values}")