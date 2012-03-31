# Project Euler
# 
# 1. Add all the natural numbers below one thousand that are multiples of 3 or 5

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
        
x = Euler3(600851475143)
# x = Euler3(23233414)

print x.solve(x.composite)