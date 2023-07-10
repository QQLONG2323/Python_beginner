from tools import BMI

def main() -> None:
    b1 = BMI("余友中", h = 174, w = 62, age = 66)
    print(b1.info())
    print(b1.bmi)
    
    
if(__name__ == "__main__"):
    main()
   
   