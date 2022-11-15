class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def addition(self):
        return self.a + self.b
    
    def multiplication(self):
        return self.a * self.b
    
    def division(self):
        return self.a / self.b
    
    def subtraction(self):
        return self.a - self.b

a, b = map(float,input("Введите два числа через пробел").split())

arg = Math(a, b)

print('addition = ', arg.addition())
print('multiplication =', arg.multiplication())
print('division =', arg.division())
print('subtraction =', arg.subtraction())
