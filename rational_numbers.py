import math

class rationals:
    def __init__(self, numerator = 0, denominator=1):
        self.num = numerator
        self.den = denominator
        self.reduce()
    def fractional_part(self):
        if self.den == 1:
            return rationals()
        elif self.num > 0:
            q = self.num//self.den
            return rationals(self.num-q*self.den, self.den)
        else:
            
            return rationals(1)-self.neg().fractional_part()

    def is_int(self):
        return self.den==1
    def reduce(self):
        if (self.den < 0):
            self.den *= -1
            self.num *= -1

        g = math.gcd(self.num, self.den)
        self.num //= g
        self.den //= g

    def neg(self):
        return rationals(-self.num,self.den)
        
    def __add__(self, other):
        sum = rationals(self.num * other.den + other.num * self.den, self.den * other.den)
        sum.reduce()
        return sum

    def __sub__(self, other):
        diff = rationals(self.num * other.den - other.num * self.den, self.den * other.den)
        diff.reduce()
        return diff

    def __mul__(self, other):
        pro = rationals(self.num * other.num, self.den * other.den)
        pro.reduce()
        return pro

    def __truediv__(self, other):
        q = rationals(self.num * other.den, self.den * other.num)
        q.reduce()
        return q
    def __eq__(self, other):
        return self.num * other.den == self.den * other.num

    def __lt__(self, other):
        return self.num * other.den < self.den * other.num

    def __le__(self, other):
        return self.num * other.den <= self.den * other.num

    def __gt__(self, other):
        return self.num * other.den > self.den * other.num

    def __ge__(self, other):
       return self.num * other.den >= self.den * other.num

    def __str__(self):
        return f"{self.num}/{self.den}"
    def disp(self):
        if self.den == 1:
            print(str(f"{self.num}"), end=' ')
        else:
            print(str(f"{self.num}/{self.den}"), end=' ')
    
