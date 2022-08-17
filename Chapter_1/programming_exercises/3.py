# Overloaded arithmetic operators for subtraction, multiplication, and true division

def gcd(m, n):
    """Finds the greatest common divisor of two given integers m and n"""
    while m % n != 0:
        m, n = n, m % n
    return n

class Fraction:
    """Class Fraction"""

    def __init__(self, num, den):
        """Constructor definition"""
        divisor = gcd(num, den)
        self.num = num // divisor
        self.den = den // divisor

    def __str__(self):
        """String representation of a Fraction"""
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        """Add two fractions together"""
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """Subtract a fraction from another"""
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        """Multiply two given fractions together"""
        new_num = self.num * other.num
        new_den = self.den *  other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        """Dividing a fraction from another"""
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def get_num(self):
        """Returns the numerator"""
        return self.num

    def get_den(self):
        """Returns the denominator"""
        return self.den

f1 = Fraction(1, 2)
f2 = Fraction(1, 4)
print(f1 / f2)