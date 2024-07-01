# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

from datetime import date

today = date.today()

class Person:        
    def __init__(self, name:str, country:str, dob:date):
        self.name = name
        self.country = country
        self.dob = dob
    
    def calculate_age(self, today):
        age = today.year - self.dob.year
        if today < date(today.year, self.dob.month, self.dob.day):
            age -= 1
        return age
    
person1 = Person('Carol', 'Australia', date(1993, 10, 20))
person2 = Person('Sarp', 'Australia', date(1992, 3, 18))

print(f'Person 1\nName: {person1.name}\nCountry: {person1.country}\nDOB: {person1.calculate_age(today)}\n')

print(f'Person 2\nName: {person2.name}\nCountry: {person2.country}\nDOB: {person2.calculate_age(today)}')