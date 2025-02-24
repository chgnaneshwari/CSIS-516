import math
import random

# Math Calculations
print("Math Calculations:")

# 1. The square root of 144
sqrt_144 = math.sqrt(144)
print(f"The square root of 144 is {sqrt_144}")

# 2. The exponential value of 2 (e^2)
exp_2 = math.exp(2)
print(f"The exponential value of 2 (e^2) is {exp_2}")

# 3. The sine and cosine values of π/4 radians
sin_pi_4 = math.sin(math.pi / 4)
cos_pi_4 = math.cos(math.pi / 4)
print(f"The sine of π/4 is {sin_pi_4}")
print(f"The cosine of π/4 is {cos_pi_4}")

# 4. The remainder of 123 divided by 17 using fmod
remainder = math.fmod(123, 17)
print(f"The remainder of 123 divided by 17 using fmod is {remainder}")

# Ask user to input radius of a circle
radius = float(input("\nEnter the radius of the circle: "))

# 5. The area and circumference of the circle
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f"The area of the circle is {area}")
print(f"The circumference of the circle is {circumference}")

# String Manipulations
print("\nString Manipulations:")

# 6. Ask user to input a sentence
sentence = input("Enter a sentence: ")

# 7. Convert sentence to lowercase
lowercase_sentence = sentence.lower()
print(f"The sentence in lowercase: {lowercase_sentence}")

# 8. Count the number of vowels
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in sentence if char in vowels)
print(f"The number of vowels in the sentence: {vowel_count}")

# 9. Reverse the sentence
reversed_sentence = sentence[::-1]
print(f"The reversed sentence: {reversed_sentence}")

# Name Handling
print("\nName Handling:")

# 10. Ask user to input their full name
full_name = input("Enter your full name: ")

# 11. Split and print first and last names
first_name, last_name = full_name.split()
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")

# 12. Create email address
email = f"{first_name.lower()}.{last_name.lower()}@CSIS516.com"
print(f"Your email address: {email}")

# Guess the Word
print("\nGuess the Word:")

# 13. Ask user to input a word
word = input("Enter a word: ")

# 14. Shuffle the letters in the word
shuffled_word = ''.join(random.sample(word, len(word)))
print(f"The shuffled word is: {shuffled_word}")

# Working with Objects
print("\nWorking with Objects:")

# 15. Ask user to input a character
char = input("Enter a character: ")

# 16. Print the ASCII value of the character
ascii_value = ord(char)
print(f"The ASCII value of '{char}' is {ascii_value}")

# 17. Ask user to input an ASCII value
ascii_input = int(input("Enter an ASCII value: "))

# 18. Convert ASCII value back to a character
character = chr(ascii_input)
print(f"The character corresponding to ASCII value {ascii_input} is '{character}'")

# Simple Calculator
print("\nSimple Calculator:")

# 19. Ask user to input two numbers and an operator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

# 20. Perform the calculation and handle division by zero
try:
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            result = None
        else:
            result = num1 / num2
    else:
        print("Error: Invalid operator.")
        result = None

    if result is not None:
        print(f"The result of {num1} {operator} {num2} is {result}")

except Exception as e:
    print(f"Error: {e}")
