"""
24. Write a Python program to test whether a passed letter is a vowel or not.
"""

def check_vowel(char):
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False

char = input("Enter the character you'd like to evaluate: ")

print(check_vowel(char))