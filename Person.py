

# Наследование

# class Person:
 
#     def __init__(self, name):
#         self.__name = name   # имя человека
 
#     @property
#     def name(self):
#         return self.__name
     
#     def display_info(self):
#         print(f"Name: {self.__name} ")


# class Em(Person):

#     def work(self):
#         print(f"{self.name} works")

# tom = Em("Tommy")
# tom.work()
# tom.display_info()
# print(tom.name)

# Композиция

# class Engine:
#     def start(self):
#         return "Двигатель запущен"

#     # def stop(self):
#     #     return "Двигатель остановлен"
    
# class Wheel: 
#     def __init__(self, position):
#         self.position = position
    
#     def rotate(self):
#         return f"Колесо {self.position} вращается"
    
# class Car:
#     def __init__(self):
#         self.ingine = Engine()
#         self.wheels = [Wheel(f"переднее {i + 1}") for i in range(2)] + \
#                     [Wheel(f"заднее {i + 1}") for i in range(2)]
        
#     def start(self):
#         return self.ingine.start()
    
#     def drive(self):
#         return ", ".join(wheel.rotate() for wheel in self.wheels)
    
#     def stop(self):
#             return "Пиздыкс, Въебались!"

# car = Car()
# print(car.start())
# print(car.drive())
# print(car.stop())


#  Геттеры и Сеттеры


