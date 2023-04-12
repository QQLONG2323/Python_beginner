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
    
class Student(Person):
    def __init__(self, n, Chinese, English, Math, **kwargs) -> None:
        super().__init__(n, **kwargs)
        self.Chinese = Chinese
        self.English = English
        self.Math = Math
    
    @property
    def total(self) -> float:
        return self.Chinese + self.English + self.Math
    
    @property
    def average(self) -> float:
        return round(self.total / 3, ndigits = 2) 
    
    @property
    def ggg(self) -> str:
        print("ggggggggg")
