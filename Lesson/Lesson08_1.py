# 此版本跟Lesson08_1.ipynb相比，比較兩光

import random
def playGame():
    print("====================猜數字遊戲====================\n")
    min = 1
    max = 100
    random_num = random.randint(min, max)
    used_num = 0

    while(True):
        keyin_value = input(f"猜數字範圍{min}~{max}: ")
        used_num += 1
        if(min <= int(keyin_value) <= max):
            if(int(keyin_value) == random_num):
                print(f"賓果!猜對了, 答案是{int(keyin_value)}\n您猜了{used_num}次\nGame Over!")
                break
            elif(int(keyin_value) > random_num):
                print(f"再小一點\n您已經猜了{used_num}次")
                max = int(keyin_value) - 1
            else:
                print(f"再大一點\n您已經猜了{used_num}次")
                min = int(keyin_value) + 1
        else:
            print("超出範圍了!")
            continue

while(True):
    playGame()
    input_key = input("立即結束遊戲,請按「q」。按其它按鈕繼續遊戲!")
    if input_key == 'q':
        break
print("遊戲結束")