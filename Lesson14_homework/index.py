from tools import Student

def main() -> None:
    a1 = Student("余友中", 99.9, 10.56, 100, age = 66)
    print(a1.info())
    print(f"國文分數: {a1.Chinese}")
    print(f"英文分數: {a1.English}")
    print(f"數學分數: {a1.Math}")
    print(f"成績加總: {a1.total}")
    print(f"成績平均: {a1.average}")
    print(a1.ggg)
    
    
    
if(__name__ == "__main__"):
    main()
   
   