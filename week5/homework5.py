class Roman_Numeral:
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

    def add(self, st1, st2):
        num1 = self.roman_to_int(st1)
        num2 = self.roman_to_int(st2)
        print(num1 + num2)

    def sub(self, st1, st2):
        num1 = self.roman_to_int(st1)
        num2 = self.roman_to_int(st2)
        print(num1 - num2)

    def mul(self, st1, st2):
        num1 = self.roman_to_int(st1)
        num2 = self.roman_to_int(st2)
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

    def area(self):
        return self.sides[0] * self.sides[1]


class Rectangle(Quadrilateral):
    def __init__(self):
        super().__init__()


class Square(Quadrilateral):
    def __init__(self):
        super().__init__()

    def input_sides(self, side):
        super().input_sides([side[0], side[0]])
