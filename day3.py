from data.day3 import data
import re

def process_data():
    result = re.findall("mul\(\d+,\d+\)", data)
    return result

def parse_nums(line):
    nums = re.findall("\d+", line)
    return list(map(int, nums))

def multiply_nums(nums):
    return nums[0] * nums[1]

if __name__ == '__main__':
    data = process_data()
    # Part 1
    sum = 0
    for line in data:
        nums = parse_nums(line)
        product = multiply_nums(nums)
        sum += product
    print(sum)