# Implemented get_num and get_den methods in Fraction

def gcd(m, n):
    """Finds the greatest common divisor of two given integers m and n"""
    while m % n != 0:
        m, n = n, m % n
    return n

class Fraction:
    """Class Fraction"""
    def __init__(self, num, den):
        """Constructor definition"""
        self.num = num
        self.den = den

    def __str__(self):
        """String representation of a Fraction"""
        return f"{self.num}/{self.den}"

    def get_num(self):
        """Returns the numerator"""
        return self.num

    def get_den(self):
        """Returns the denominator"""
        return self.den