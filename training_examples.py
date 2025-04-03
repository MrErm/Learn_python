# Определите класс Rectangle, который представляет прямоугольник. 
# Через конструктор класс принимает ширину и длину и сохраняет их в атрибутах width и length соответственно. 
# Также этом классе определите метод area, который возвращает площадь прямоугольника,
# и метод perimeter, который возвращает периметра прямоугольника.
# После создания класса определите несколько объектов класса Rectangle и продемонстрируйте работу его методов.


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def area(self):
        print(f"Площать = {self.width * self.length}")

s = Rectangle(5,5)
s.area()


#  Конвертер арабских цифр в римские 

def decimal_to_roman(decimal):
    
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'),(9, 'IX'),(5, 'V'),(4, 'IV'),(1, 'I')
    ]
    roman = ""
    for value, numeral in roman_numerals:
        
        while decimal >= value:
            roman += numeral
            decimal -= value
            print(f"roman = {roman}, decimal = {decimal} ")
    return roman

decimal_number = int(input("Введите число: "))

roman_number = decimal_to_roman(decimal_number)
print(f"Число {decimal_number} это \
{roman_number} в Римских цифрах.")



# Угадай число с помощью модуля random

import random
def guessing_game ():
    answer = random.randint(0, 5)

while True:
    user_guess = int (input("Введи число:"))

    if user_guess == answer:
        print(f"Правильно! Ответ {user_guess}")
        break

    if user_guess < answer:
        print(f"Число {user_guess} слишком маленькое, еще раз!")

    else:
        print(f"Число {user_guess} слишком большое, еще раз!")

guessing_game()


# Списки, методы, функции, f-строки, циклы


list = []
program = ['Pethon', 'C#', 'C', 'C++', 'Java', 'Scala', 'Golang', 'Rust', 'JS']
num = [1,2,3,4,5,6,7,8,9]
test = ['car', 'bus', 'cat']
others = [1,'C#', test]


split = '1/2//3/4/5//6///7'
list = split.split('//')
print(list)

program = ['Python', 'C#', 'C', 'C++', 'Java', 'Scala', 'Golang', 'Rust', 'JS']
result = program[::2]
print(result)

def sum(a, b):
    sum = a + b
    return sum
a = sum(5, 6)
print(a)

def person(name, age, company):
    print(f"Name: {name} Age: {age} Company: {company}")

tom = ("Tom", 22, "Google")
person(*tom)

