print("請輸入2數, 求2數公因數: ")
n = int(input("請輸入第一個數字: "))
m = int(input("請輸入第二個數字: "))
print(f"結果:==============\n{n}和{m}的公因數是: ", end="")

if(n <= m):
    a = n
else:
    a = m

for i in range(1, a+1):
    if(n % i == 0 and m % i == 0):
        print(i, end="  ")