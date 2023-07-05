import random

def lottery(): 
    nums = set()
    while(len(nums) < 7):
        nums.add(random.randint(1, 49))
    list_nums = list(nums) #加list才有索引
    return list_nums