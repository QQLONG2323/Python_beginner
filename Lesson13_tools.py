class Person():
    def __init__(self, name, age, isMan) -> None:
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
    
    @age.setter
    def age(self, input_value):
        if(0 < input_value <= 100):
            self.__age = input_value
    
    @property
    def sex(self):
        if(self.__isMan):
            return "男"
        else:
            return "女"
        
    #override(覆寫)父類別的method
    def __repr__(self) -> str:
        own = super().__repr__()
        return f"我是Person類別建出來的實體\n{own}"
