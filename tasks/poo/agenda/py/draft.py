class Fone:
    def __init__(self, id: str, number: str):
        self.__id = id
        self.__number = number
    def getId(self):
        return self.__id
    def getNumber(self):
        return self.__number
    def __str__(self) -> str:
        return f"[{self.__id}:{self.__number}]"
class Contact:
    def __init__(self, name: str):
        self.__name = name
    def addFone(self, id: str, number: str):
    def getFone(self):
        self.fone: list[Fone] = []
    def getName(self):
        return self.__name
    def setName(self, name: str):
        self.__name = name
    def __str__(self) -> str:
        return f"{self.__name} {self.fone}"