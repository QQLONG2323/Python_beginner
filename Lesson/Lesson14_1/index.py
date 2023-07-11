from tools import BMI, Student

def main() -> None:
    b1 = BMI("余友中", h = 174, w = 62, age = 66)
    print(b1.info())
    print(b1.name)
    print(b1.bmi)

    s1 = Student('AAA', chinese = 67, english = 78, math = 68, isMan = False)   
    print(f'總分: {s1.sum}')
    print(s1.age)
    print(f'平均: {s1.average}')
    print(s1.sex)
    
    
if(__name__ == "__main__"):
    main()   