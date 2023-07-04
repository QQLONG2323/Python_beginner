age = input("輸入年齡: ")

if(age == ""):
    print("普遍級")
elif(int(age) >= 18):
    print("限制級")
elif(int(age) >= 13):
    print("輔導級")
elif(int(age) <= 12):
    print("普遍級")