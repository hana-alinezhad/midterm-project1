# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:55:21 2024

@author: Hana
"""

class CustomStr:
    def __init__(self, value):
        self.value = value

    def custom_split(self, delimiter=' '):
        return self.value.split(delimiter)

    def remove_duplicate(self):
        result =[]
        for char in self.value:
            if char not in result:
                result.append(char)
        return ''.join(result)

    def set_value(self, new_value):
        self.value = new_value

    def is_float(self):
        try:
            float(self.value)
            return True
        except:
            return False

    def is_palindrome(self):
        cleaned_value = ''.join(filter(str.isalnum, self.value)).lower()
        return cleaned_value == cleaned_value[::-1]

#example

custom_string = CustomStr("A man a plan a canal Panama")
print(custom_string.custom_split())
print(custom_string.remove_duplicate())
print(custom_string.is_float())
print(custom_string.is_palindrome())
