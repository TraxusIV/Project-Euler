# Project Euler

from math import *

class Euler1(object):
    """
    Add all the natural numbers below one thousand that are multiples of 3 or 5
    """
    def __init__(self, limit):
        self.limit = limit
    def solve(self):
        """returns answer"""
        answer = 0
        for i in range(self.limit):
            if (i % 3 == 0) or (i % 5 == 0):
                answer += i
        return answer

class Euler2(object):
    """
    By considering the terms in the Fibonacci sequence whose values do not 
    exceed four million, find the sum of the even-valued terms.
    """
    def __init__(self, limit):
        self.limit = limit
    def solve(self):
        """returns answer"""
        seq = []
        i = 0
        j = 1
        while i < self.limit:
            seq.append(i)
            j = j + i
            i = j - i
        return sum([x for x in seq if x % 2 == 0])

class Euler3(object):
    """
    Find the largest prime factor of a composite number
    """
    
    def __init__(self, composite):
        self.composite = composite
    
    def isOdd(self, number):
        if str(number)[-1] in set(['1','3','5','7','9']):
            return True
        else:
            return False
    
    def isSquare(self, number):
        if number < 0:
            return False
        else:
            return sqrt(number).is_integer()
    
    def solve(self, number):
        if number % 2 == 0:
            i = number / 2
        else:
            i = (number + 1) / 2
        while i > 1:
            if self.isOdd(i) and (number % i == 0):
                return self.solve(i)
            else:
                i = i - 1
        return number
        
    def Fermat(self, number):
        if self.isOdd(number):
            n = number
        else:
            n = (number / 2) - 1
        a = ceil(sqrt(n))
        b2 = (a * a) - n
        while not self.isSquare(b2):
            a = a + 1
            b2 = (a * a) - n
        return int(a - sqrt(b2))
            
class Euler4(object):
    """
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    def __init__(self, digits):
        self.digits = digits
        limitList = ([9] * digits)
        self.limit = 1000 
    
    def solve(self):
        products = []
        palindromes = []
        for i in range(1000):
            for x in range(1000):
                products.append(i * x)
        for j in products:
            if str(j) == str(str(j)[::-1]):
                palindromes.append(j)
        return max(palindromes)
                
        
x = Euler4(3)
print x.limit    
print x.solve()