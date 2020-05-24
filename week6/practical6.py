from math import pi
import re


class Circle:
    def __init__(self, rad, color):
        assert isinstance(rad, (int, float)), "Rad must be set to an integer or float"
        assert isinstance(color, str), "Color must be set to an string"
        self.r = rad
        self.c = color

    def __str__(self):
        return '{}{}{}{}'.format("A ", self.c, " circle with radius ", self.r)

    def area(self):
        return pi * self.r ** 2

    def circumference(self):
        return 2 * pi * self.r

    def __sub__(self, b):
        return Circle(self.r - b.r, self.c)


c = Circle(3.4, 'red')
k = Circle(2, 'blue')
d = c - k
print(d)
print("Area is: ", c.area())
print("Circumference is: ", c.circumference())
print(c)


class RomanNumber():
    def __init__(self, s):
        assert isinstance(s, str), "Number must be set to an string"
        assert self.checkIfRomanNumeral(s), "Invalide roman number"
        self.num = s

    def checkIfRomanNumeral(self, s):
        numeral = s.upper()
        thousand = 'M{0,3}'
        hundred = '(C[MD]|D?C{0,3})'
        ten = '(X[CL]|L?X{0,3})'
        digit = '(I[VX]|V?I{0,3})'
        return (bool(re.match(thousand + hundred + ten + digit, numeral)))

    def rom_to_int(self):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(self.num)):
            if i > 0 and rom_val[self.num[i]] > rom_val[self.num[i - 1]]:
                int_val += rom_val[self.num[i]] - 2 * rom_val[self.num[i - 1]]
            else:
                int_val += rom_val[self.num[i]]
        return int_val

    def int_to_rom(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

    def __str__(self):
        return '{}{}'.format("A roman number is ", self.num)

    def __add__(self, x):
        return RomanNumber(self.int_to_rom(self.rom_to_int() + x.rom_to_int()))

    def __sub__(self, x):
        assert self.rom_to_int() < x.rom_to_int(), " First number must be bigger then second"
        return RomanNumber(self.int_to_rom(self.rom_to_int() - x.rom_to_int()))

    def __mul__(self, x):
        return RomanNumber(self.int_to_rom(self.rom_to_int() * x.rom_to_int()))

    def __floordiv__(self, x):
        return RomanNumber(self.int_to_rom(self.rom_to_int() // x.rom_to_int()))

    def __pow__(self, x):
        return RomanNumber(self.int_to_rom(self.rom_to_int() ** x.rom_to_int()))


class Person:
    def __init__(self, name, last_name, age, gender, student, password):
        assert isinstance(name, str), "Name attribute must be set to an string"
        assert isinstance(last_name, str), "Last name attribute must be set to an string"
        assert isinstance(age, int), "Age attribute must be set to an int"
        assert isinstance(gender, str), "gender attribute must be set to an string"
        assert isinstance(student, bool), "Student attribute must be set to an bool"
        assert isinstance(password, str), "Password attribute must be set to an string"
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student = student
        self.__pass = password

    def Greeting(self, second_person):
        print("Welcome ", second_person.name)

    def Goodbye(self):
        print("Bye everyone!")

    def Favourite_num(self, num1):
        return '{}{}'.format("My favorite number is ", str(num1))

    def Read_file(self, filename):
        assert isinstance(filename, str), "Filename must be set to an string"
        try:
            f = open(filename + '.txt')
        except FileNotFoundError:
            print("File Not Found Error")


class Polygon:
    def __init__(self, n):
        assert isinstance(n, int), "Side attribute must be set to an int"
        self.n = n
        self.sides = list()

    def input_sides(self, sides):
        assert isinstance(sides, list), "Sides attribute must be set to an list"
        self.sides = sides
        assert len(sides) == self.n, "Invalide sides count"

    def get_perimeter(self):
        return sum(self.sides)

    def __str__(self):
        return '{}{}{}{}'.format("Sides ", self.sides, " perimetr is ", self.get_perimeter())


class Quadrilateral(Polygon):
    def __init__(self):
        super().__init__(4)


class Rectangle(Quadrilateral):
    def __init__(self):
        super().__init__()

    def input_sides(self, side):
        super().input_sides(side * 2)

    def area(self):
        return self.sides[0] * self.sides[1]


class Square(Quadrilateral):
    def __init__(self):
        super().__init__()

    def input_sides(self, side):
        super().input_sides(side * 4)

    def area(self):
        return self.sides[0] ** 2
