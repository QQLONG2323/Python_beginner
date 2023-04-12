n = eval(input("讓使用者輸入直角三角形的對邊: "))
m = eval(input("讓使用者輸入直角三角形的斜邊: "))
import math
print("直角三角形的角度為: ", math.ceil(math.degrees(math.asin(n/m))), "degree")