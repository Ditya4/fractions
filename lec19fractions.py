'''
>>> Fraction(2, 0)
Traceback (most recent call last):
  ...
ZeroDivisionError: Denominator, equal to zero, not allowed.
>>> x, y = fraction_reduction(4, 8)
>>> x
1
>>> y
2
>>> x, y = fraction_reduction(5, 25)
>>> x
1
>>> y
5
>>> test = Fraction(4, 8)
>>> print(test)
1 / 2
>>> test = Fraction(8, 4)
>>> print(test)
2
>>> test = Fraction(12, 10)
>>> print(test)
1 1 / 5
>>> print(Fraction("10", 10))
1
>>> print(Fraction(10, "10"))
1
>>> print(Fraction("15", "10"))
1 1 / 2
>>> print(Fraction("adsf", 15))
Traceback (most recent call last):
    ...
ValueError: Can't convert numerator into a fraction.
>>> print(Fraction("15", "adsf"))
Traceback (most recent call last):
    ...
ValueError: Can't convert denominator into a fraction.
>>> print(Fraction("adsf", "!@#!@#"))
Traceback (most recent call last):
    ...
ValueError: Can't convert numerator into a fraction.
>>> print(Fraction("-185", "10"))
-18 1 / 2
>>> print(Fraction("185", "-10"))
-18 1 / 2
>>> print(Fraction("-185", "-10"))
18 1 / 2
>>> test = Fraction("-185", "10")
>>> test1 = Fraction("185", "-10")
>>> test2 = Fraction(-185, -15)
>>> print(test == test1)
True
>>> print(test2 == test1)
False
>>> print(test != test1)
False
>>> print(test2 != test1)
True

>>> frac_1_2 = Fraction("1", "2")
>>> frac_minus_1_2 = Fraction(-1, 2)
>>> frac_1_3= Fraction("1", "3")
>>> frac_1_4 = Fraction(1, 4)
>>> print(frac_1_2 < frac_1_3)
False
>>> print(frac_1_3 < frac_1_4)
False
>>> print(frac_1_4 < frac_1_2)
True
>>> print(frac_1_3 < frac_1_3)
False
>>> print(frac_1_3 < frac_minus_1_2)
False
>>> print(frac_1_3 <= frac_1_3)
True
>>> print(frac_minus_1_2 >= frac_minus_1_2)
True
>>> print(frac_1_3 <= frac_1_4)
False
>>> print(-frac_minus_1_2)
1 / 2
>>> print(abs(frac_1_2), abs(-frac_1_2), abs(frac_minus_1_2))
1 / 2 1 / 2 1 / 2
>>> print(frac_1_2 * frac_1_3)
1 / 6
>>> print(frac_1_2 / frac_1_3)
1 1 / 2
>>> print(frac_1_2 + frac_1_2)
1
>>> print(frac_1_2 + frac_1_3)
5 / 6
>>> print(frac_1_2 + frac_minus_1_2)
0
>>> print(frac_1_2 - frac_1_3)
1 / 6
>>> print(1 + frac_1_2)
1 1 / 2
>>> print(1 + frac_minus_1_2)
1 / 2
>>> print(frac_minus_1_2 + 1)
1 / 2
>>> print(frac_minus_1_2 - 1)
-1 1 / 2
>>> print(frac_minus_1_2 - 1.2)
-1 1 / 2





Created on 21  2022
запис формою  вверх-вниз типа число
Скорочення дробів під час друку
Друк дробів
Цілі числа друкувалися без дробової частини
Райзати стандартні помилки ділення на 0, не числові вхідні дані , Не цілі
Функції більше менше Рівне не Рівне
Конструктор дробів має пиймати стрічку інт флоат
Унарний мінус
Функція ABS
дія додавання, віднімання, множення, ділення, праве додавання
для додавання і віднімання реалізував роботу з інтом та флоатом
Дія дробів using Magic метод праве віднімання, праве множення, праве ділення
Функція приведення до спільного знаменника що вона не the потрібна і просто
множити
Операції з integer і float

реалізація скорочення дробів, в функції стр туфта, там
О(значення мін(чисальник, знаменник)) пишу 2 функції:
_gcd і str_2 які скорочують за ~O(1) підключати їх не буду, але щоб була
правильна реалізація
@author: dno
'''
import doctest


class Fraction:

    def __init__(self, numerator, denominator):
        '''
        If the type of numerator or denominator is str we try to convert it
        into integer if we could we pass by, if can't — raise ValueError.
        If the denominator is equal to zero we rise ZeroDivisionError.
        If the operand is float type, it is converted into an int by
        throwing out fraction part.
        unary minus will be stored in the numerator(denominator is always
        positive number)
        '''
        if type(numerator) == float:
            numerator = int(numerator)
        if type(denominator) == float:
            denominator = int(denominator)

        if type(numerator) == str:
            try:
                numerator = int(numerator)
            except ValueError:
                raise ValueError("Can't convert numerator into a fraction.")
        if type(denominator) == str:
            try:
                denominator = int(denominator)
            except ValueError:
                raise ValueError("Can't convert denominator into a fraction.")

        if denominator == 0:
            raise ZeroDivisionError("Denominator, equal to zero, not allowed.")

        self.numerator = numerator
        if denominator < 0:
            self.numerator = -self.numerator
            denominator = abs(denominator)
        self.denominator = denominator

    def __str__(self):
        '''
        if fraction > 1 we return numerator // denominator as integer
        and send to fraction_reduction() only < 1 part of fraction:
        self.numerator % self.denominator, self.denominator
        if fraction is negative we add - to result and work with positive
        numerator and denominator.
        '''

        if self.numerator < 0:
            result = "-"
            numerator = abs(self.numerator)
        else:
            numerator = abs(self.numerator)
            result = ""
        if numerator % self.denominator == 0:
            result += str(numerator // self.denominator)
        elif numerator / self.denominator < 1:
            numerator, denominator = fraction_reduction(
                numerator, self.denominator)
            result += str(numerator) + " / " + str(denominator)
        elif numerator / self.denominator > 1:
            numerator, denominator = fraction_reduction(
                abs(self.numerator) % self.denominator, self.denominator)
            # print(numerator, denominator)
            result += (str(abs(self.numerator) // self.denominator) +
                       " " + str(numerator) + " / " + str(denominator))
        return result

    def str_2(self):
        gcd = Fraction._gcd(self.numerator, self.denominator)
        return Fraction(self.numerator // gcd, self.denominator // gcd)

    def _gcd(first, second):
        while second != 0:
            first, second = second, first % second
        return first

    def __eq__(self, other):
        numerator_1, denominator_1 = fraction_reduction(self.numerator, self.denominator)
        numerator_2, denominator_2 = fraction_reduction(other.numerator, other.denominator)
        if (numerator_1 == numerator_2 and
                denominator_1 == denominator_2):
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return (self.numerator * other.denominator <
                other.numerator * self.denominator)

    def __gt__(self, other):
        return (self.numerator * other.denominator >
                other.numerator * self.denominator)

    def __le__(self, other):
        return (self.numerator * other.denominator <
                other.numerator * self.denominator or
                self.__eq__(other))

    def __ge__(self, other):
        return (self.numerator * other.denominator >
                other.numerator * self.denominator or
                self.__eq__(other))

    def __neg__(self):
        if self.numerator <= 0:
            numerator = abs(self.numerator)
        else:
            numerator = -self.numerator
        result = Fraction(numerator, self.denominator)
        return result

    def __abs__(self):
        return Fraction(abs(self.numerator), self.denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        result = Fraction(numerator, denominator)
        return result

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        result = Fraction(numerator, denominator)
        return result

    def __add__(self, other):
        if type(other) == float:
            other = int(other)
        if type(other) == int:
            other = Fraction(other, 1)
        print("\n__add self=", self, "with type", type(self), "other", other)
        print("self.numerator", self.numerator, "self.denominator",
              self.denominator)
        numerator_self = self.numerator * other.denominator
        numerator_other = other.numerator * self.denominator
        bouth_denominator = self.denominator * other.denominator
        numerator = numerator_self + numerator_other
        result = Fraction(numerator, bouth_denominator)
        return result

    def __radd__(self, other):
        """
        !!!!!
        self тут це другий операнд, тобто фракшн, значить я передаю в
        функцію адд замість селфа азер(інт там є селфом), але воно правильно
        рахує, я не розумію чому.
        по суті тут має бути return Fraction.__add__(self, other)
        тоді фракшн йде пеншою, а інт другим
        """
        print("\n__radd self=", self, "other", other)
        return Fraction.__add__(other, self)

    def __sub__(self, other):
        if type(other) == float:
            other = int(other)
        if type(other) == int:
            other = Fraction(other, 1)

        numerator_self = self.numerator * other.denominator
        numerator_other = other.numerator * self.denominator
        bouth_denominator = self.denominator * other.denominator
        numerator = numerator_self - numerator_other
        result = Fraction(numerator, bouth_denominator)
        return result

    def __rsub__(self, other):
        return Fraction.__add__(-other, self)

    def __pow__(self, power):
        return Fraction(self.numerator ** power, self.denominator ** power)







def fraction_reduction(numerator, denominator):
    if numerator < 0:
        negative = True
        numerator = abs(numerator)
    else:
        negative = False
    divider = 2
    while divider <= min(numerator, denominator):
        if numerator % divider == 0 and denominator % divider == 0:
            numerator //= divider
            denominator //= divider
        else:
            divider += 1
    if negative:
        numerator = -numerator
    return numerator, denominator










doctest.testmod()

frac_1_2 = Fraction("1", "2")
frac_minus_1_2 = Fraction(-1, 2)
frac_1_3 = Fraction("1", "3")
frac_1_4 = Fraction(1, 4)

# print(frac_1_2, "+", 1, "= ", end="")
# print(frac_1_2 + 1)

print(2, "+", frac_1_2, "= ", end="")
print(2 + frac_1_2)

# print(frac_minus_1_2, "-", 1.2, "= ", end="")
# print(frac_minus_1_2 - 1.2)


# print(abs(frac_1_2), abs(-frac_1_2), abs(frac_minus_1_2))
# test = Fraction("1", "2")
# print(test)
# test1 = Fraction("-1", "3")
# print(test1)
# test2 = Fraction(1, 4)
#===============================================================================
# print(test, "<=", test1)
# print(test <= test1)
# print(test1, "<=", test2)
# print(test1 <= test2)
# print(test2, "<=", test2)
# print(test2 <= test2)
#===============================================================================



# ==============================================================================
# test = Fraction(2, 0)
# print(test)
# numerator, denominator = fraction_reduction(5, 25)
# print(numerator, denominator)
# ==============================================================================















