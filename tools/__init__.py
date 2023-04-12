import random

def lottery(): 
    nums = set()
    while(len(nums) <= 6):
        nums.add(random.randint(1, 49))
    return nums