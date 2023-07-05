#請輸入本期大樂透電腦選號的組數:10
import Lesson11_3_tools

for n in range(int(input("請輸入大樂透組數: "))):
    values = Lesson11_3_tools.lottery()
    print(f"目前為第 {n+1} 組: \n號碼為: {values[:6]}; \n特別號為: {values[-1:]}。")

print()
print("!!!!!!!!!!!!!!!祝您中大獎!!!!!!!!!!!!!!!")