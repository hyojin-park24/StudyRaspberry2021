class Person(object):
    total = 0

    def __init__(self, name, age): #기본생성자 (self) / 오버로딩 
        self.name = name
        self.age = age

    def getAge(self):
        return self.age

class Man(Person):
    gender = 'male'

class Korean(Person):
    nationality = 'Korea'

class KoreanMan(Man, Korean):
    pass