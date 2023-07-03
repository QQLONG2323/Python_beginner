scores = int(input("請輸入成績(0-100): "))

if(scores >= 60):
    if(scores >= 90):
        print("優等")
    if(scores < 90):
        if(scores >= 80):
            print("甲等")
    if(scores <80):
        if(scores >= 70):
            print("乙等")
        else:
            print("丙等")
else:
     print("丁等")