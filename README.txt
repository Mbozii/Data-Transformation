

This is an exercise on Data Transformation.

Exercise:

You’re given:
nums = [4, 9, 13, 18, 7, 2, 15, 20]

Your task:

1. If the number is divisible by 3, multiply it by 5
2. If it’s even but not divisible by 3, divide it by 2
3. If it’s odd and not divisible by 3, add 7
4. Store all results in a new list
5. From that new list, create another list with values that are between 10 and 50 (inclusive)
6. Print both lists


Code:

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



Explanation:

mod_nums = []
This is an empty list. We’ll use it to store the modified values after applying the transformation rules to each number in nums.


values = []
Another empty list, which we’ll use to store only those transformed numbers that fall between 10 and 50, inclusive.


for i in range(len(nums)):
This is a loop that goes through the list nums one item at a time using its index (i).

len(nums) gives us the total number of elements in the list.

range(len(nums)) creates a sequence of numbers from 0 to the last index in nums.

So, nums[i] gives us the actual number at each position as we loop through.



First Condition:
nums[i] % 3 == 0 checks if the number is divisible by 3.

If true, multiply the number by 5.

Then, add this new value to the mod_nums list.


Second Condition:
elif means “else if.” This is checked only if the first condition is false.

This condition checks if the number is even (% 2 == 0) and NOT divisible by 3 (% 3 != 0).

If true, we divide the number by 2 using integer division (//), which drops any decimal.

Then add that result to mod_nums.


Third Condition:
This is for numbers that are odd (% 2 == 1) and not divisible by 3.

If true, we add 7 to the number.

Then store it in mod_nums.



The second loop:
This loop goes through all the values in mod_nums.

It checks if each value is between 10 and 50, inclusive.

If yes, it adds that number to the values list.




Visually:

Original List (nums)
[4, 9, 13, 18, 7, 2, 15, 20]
       |
       v
For each number:
-----------------------------
| Check conditions in order: |
-----------------------------
   1) Divisible by 3? ---------> Yes ------> Multiply by 5
                            | No
   2) Even and not divisible by 3? ---> Yes ------> Divide by 2
                            | No
   3) Odd and not divisible by 3? ---> Yes ------> Add 7
                            | No (not possible here)

                            |
                            v
              Add transformed number to mod_nums:
                 [2, 45, 20, 90, 14, 1, 75, 10]

                            |
                            v
      Filter mod_nums to values between 10 and 50 (inclusive):
                   [45, 20, 14, 10]

                            |
                            v
                  Print both lists:
                 mod_nums and values







