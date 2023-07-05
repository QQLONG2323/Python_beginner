import tools

group = int(input("請輸入大樂透組數: "))
for _ in range(group):
    listlottery = list(tools.lottery())
    print(f"號碼為: {listlottery[:6]}\n特別號為:{listlottery[-1:]}")

#請輸入本期大樂透電腦選號的組數:10
import tools

for n in range(int(input("請輸入本期大樂透電腦選號的組數:"))):
    values = tools.lottery_poll()
    print(f"您將中大獎的大樂透電腦選號第{n+1}組:{values[:6]}&特別號為:{values[-1:]}")
print()
print("!!!!!!!!!!!!!!!祝您中大獎!!!!!!!!!!!!!!!")