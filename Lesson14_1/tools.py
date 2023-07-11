class Person():
    def __init__(self, name, age = 25, isMan = True) -> None:
        super().__init__()
        self.__name = name
        self.__age = age
        self.__isMan = isMan

    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    @property
    def sex(self):
        if(self.__isMan):
            return "男"
        else:
            return "女"
        
    def info(self) -> str:
        message = ""
        message += f"我的姓名是: {self.name}\n"
        message += f"我的年齡是: {self.age}\n"
        message += f"我的性別是: {self.sex}"
        return message

class BMI(Person):
    def __init__(self, n, h, w, **kwargs) -> None:
        super().__init__(n, **kwargs)
        self.height = h
        self.weight = w
    
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height/100) **2, ndigits = 2)


class Student(Person):
    def __init__(self, n, chinese, english, math, **kwargs) -> None:
        super().__init__(n, **kwargs)
        self.chinese = chinese
        self.english = english
        self.math = math

    @property #decorator property
    def sum(self) -> float:
        return self.chinese + self.english + self.math
    
    @property
    def average(self) -> float:
        return round(self.sum / 3.0, ndigits=2)