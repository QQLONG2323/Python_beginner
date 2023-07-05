# 請輸入本期大樂透電腦選號的組數:10

import random

def lottery(): 
    nums = set()
    while(len(nums) <= 6):
        nums.add(random.randint(1, 49))
    return nums

group = int(input("請輸入大樂透組數: "))
for _ in range(group):
    lottery()
    listlottery = list(lottery())
    print(f"號碼為: {listlottery[:6]}\n特別號為:{listlottery[-1:]}")