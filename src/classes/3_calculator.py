# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class Calculator:
    
    def __init__(self, num1:float, num2:float):
        self.num1 = num1
        self.num2 = num2
        
    def addition(self):
        return round((self.num1 + self.num2), 2)
    
    def subtraction(self):
        return round((self.num1 - self.num2), 2)
    
    def multiplication(self):
        return round((self.num1 * self.num2), 2)
    
    def division(self):
        if self.num2 == 0:
            return 'Can\'t divide by 0'
        return round((self.num1 / self.num2), 2)
    
combination1 = Calculator(3, 4)
combination2 = Calculator(5.773, 9.114)
combination3 = Calculator(6, 0)

print('Combination1:')
print('Addition result: ', combination1.addition())
print('Subtraction result: ', combination1.subtraction())
print('Multiplication result: ', combination1.multiplication())
print('Division result: ', combination1.division())

print('Combination2:')
print('Addition result: ', combination2.addition())
print('Subtraction result: ', combination2.subtraction())
print('Multiplication result: ', combination2.multiplication())
print('Division result: ', combination2.division())

print('Combination3:')
print('Addition result: ', combination3.addition())
print('Subtraction result: ', combination3.subtraction())
print('Multiplication result: ', combination3.multiplication())
print('Division result: ', combination3.division())