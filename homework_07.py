sum = 0
num = 0
print("顯示:========================================")
while(True):
    num += 1
    input_value = int(input(f"請輸入第{num}個數值: "))
    if(input_value % 2 == 0):
        sum += input_value
    elif(input_value < 0):
        break
    else:
        continue
print(f"所有輸入的偶數的加總是:{sum}\n=============================================")