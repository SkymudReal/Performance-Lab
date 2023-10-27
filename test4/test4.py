import sys

filename = sys.argv[1]
with open(filename, 'r') as file:
    nums = [int(num) for num in file.read().split()]

min_moves = 0
sum_nums = sum(nums)
target_num = round(sum_nums / len(nums))

for num in nums:
    min_moves += abs(num - target_num)

print(min_moves)
