class Roman_Numeral:
    def __init__(self, s):
        self.num = s

    def rom_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

    def add(self, st1):
        num1 = st1.rom_to_int(st1.num)
        num2 = self.rom_to_int(self.num)
        print(num1 + num2)

    def sub(self, st1):
        num1 = st1.rom_to_int(st1.num)
        num2 = self.rom_to_int(self.num)
        print(num1 - num2)

    def mul(self, st1):
        num1 = st1.rom_to_int(st1.num)
        num2 = self.rom_to_int(self.num)
        print(num1 * num2)


class Person:
    def __init__(self, name, last_name, age, gender, student, password):
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


class Polygon:
    def __init__(self, n):
        self.n = n
        self.sides = list()

    def input_sides(self, sides):
        self.sides = sides

    def get_perimeter(self):
        return sum(self.sides)


class Quadrilateral(Polygon):
    def __init__(self):
        super().__init__(4)


class Rectangle(Quadrilateral):
    def __init__(self):
        super().__init__()

    def input_sides(self, side):
        if side[0] != side[1] and len(side) == 2:
            super().input_sides(side * 2)
        else:
            raise Exception("Rectangle object can receive only 2 different lengths of sides")

    def area(self):
        return self.sides[0] * self.sides[1]


class Square(Quadrilateral):
    def __init__(self):
        super().__init__()

    def input_sides(self, side):
        if len(side) == 1:
            super().input_sides(side * 4)
        else:
            raise Exception("Square object can receive only 1 side")

    def area(self):
        return self.sides[0] ** 2
