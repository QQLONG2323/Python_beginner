import math
r = eval(input("請輸入圓柱體半徑(公分): "))
h = eval(input("請輸入圓柱體的高(公分): "))
a = ((r**2) * math.pi) * h
print(f"圓柱體的體積: {a:.2f} 立方公分")