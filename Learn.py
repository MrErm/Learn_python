
# Инкапсуляция

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def print_person(self):
#         print(f"Этот {self.__name}\tему {self.__age} лет")

# p = Person("Pizduk", 30)
# p.print_person

# Геттеры и Сеттеры

# class Personal:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def set_age(self, age):
#         self.__age = age

#     def get_age(self):
#         return self.__age
    
#     def get_name(self):
#         return self.__name
    
#     def print_person(self):
#         print(f"Имя: {self.__name} Возраст: {self.__age}")

# tom = Personal("Tommy", 39)
# tom.print_person()
# tom.set_age(20)
# print(tom.get_age(), tom.get_name())




# Свойства

class Pers:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            print("фэээк")

    @property
    def name(self):
        return self.__name
    
    def print_person(self):
        print(f"Имиа: {self.__name}  Возраст: {self.__age} ")

bob = Pers("Bobby", 52)

bob.age = 200

print(bob.age)

bob.print_person()

