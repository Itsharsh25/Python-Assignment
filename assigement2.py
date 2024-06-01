# 1. Write a Python method in Oop called “calculate_area” that takes the radius of a circle as input and returns the area of the circle, write program using Oop.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * (self.radius ** 2)

circle = Circle(5)
area = circle.calculate_area()
print(f"The area of the circle with radius {circle.radius} is {area:.2f}")

#2. Write a Python method in Oop called “calculate_discount” that calculates the 
# final price of an item after applying a discount percentage. The function should 
# take the original price and the discount percentage as inputs.
class Item:
    def __init__(self, original_price):
        self.original_price = original_price

    def calculate_discount(self, discount_percentage):
        discount_amount = self.original_price * (discount_percentage / 100)
        final_price = self.original_price - discount_amount
        return final_price

item = Item(100)  # Original price is 100
final_price = item.calculate_discount(20)  # Applying a 20% discount
print(f"The final price after applying the discount is {final_price:.2f}")


# 3. Write a method in Oop named “count_vowels” that takes a string as input and 
# returns the count of vowels (both uppercase and lowercase) in the string.

class Alphabet:
    def __init__(self, text):
        self.text = text

    def count_vowels(self):
        vowels = 'aeiouAEIOU'
        count = 0
        for char in self.text:
            if char in vowels:
                count += 1
        return count
    
alpha_bet = Alphabet("Hello World")
vowel_count = alpha_bet.count_vowels()
print(f"The number of vowels in the string is: {vowel_count}")


