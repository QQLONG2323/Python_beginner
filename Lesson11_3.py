import tools

group = int(input("請輸入大樂透組數: "))
for _ in range(group):
    listlottery = list(tools.lottery())
    print(f"號碼為: {listlottery[:6]}\n特別號為:{listlottery[-1:]}")