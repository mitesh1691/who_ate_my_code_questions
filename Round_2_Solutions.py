# 1. Problem Description: Check if Two Strings are Anagrams
# You are tasked with creating a Python program to determine whether two strings are anagrams of each other.
# Two strings are considered anagrams if they have the same characters with the same frequencies, ignoring spaces and case.
# The program should efficiently check if the given strings are anagrams and return the result.

# Input:
#    str1: The first string.
#    str2: The second string.

# Output:
#    Returns True if the strings are anagrams, and False otherwise.

# Example:

# Example 1
#    s1 = "listen"
#    s2 = "silent"
#    result1 = are_anagrams(s1, s2)
# Output: True

# Example 2
#    s3 = "Java"
#    s4 = "jAvA"
#    result2 = are_anagrams(s3, s4)
# Output: True

# Example 3
#    s5 = "Hello"
#    s6 = "World"
#    result3 = are_anagrams(s5, s6)
# Output: False

# Notes:
#    Solution Should be of O(n) time complexity
#    The function should consider spaces and be case-insensitive.

def are_anagrams(str1, str2):
    if str1 is None or str2 is None or len(str1) ?? len(str2):
        return ?

    char_count = [0] * ?  # Assuming only lowercase alphabets

    
    for c in ?.lower():
        if c.isalpha():
            char_count[ord(?) - ord('?')] += 1

   
    for c in ?.lower():
        if c.isalpha():
            char_count[ord(?) - ord('?')] ?? 1

    
    for count in ?:
        if count != ?:
            return False

    return ?

# Test Cases
# Test Case 1
s1 = "listen"
s2 = "silent"
print("Test Case 1: Are Anagrams?", are_anagrams(s1, s2))

# Test Case 2
s3 = "Java"
s4 = "jAvA"
print("Test Case 2: Are Anagrams?", are_anagrams(s3, s4))

# Test Case 3
s5 = "Hello"
s6 = "World"
print("Test Case 3: Are Anagrams?", are_anagrams(s5, s6))

# Test Case 4
s7 = "Astronomer"
s8 = "Moon starer"
print("Test Case 4: Are Anagrams?", are_anagrams(s7, s8))

# Test Case 5
s9 = "AABB"
s10 = "ABAB"
print("Test Case 5: Are Anagrams?", are_anagrams(s9, s10))

# Test Case 6
s11 = "A gentleman"
s12 = "Elegant man"
print("Test Case 6: Are Anagrams?", are_anagrams(s11, s12))

# Test Case 7
s13 = "Debit card"
s14 = "Bad credit"
print("Test Case 7: Are Anagrams?", are_anagrams(s13, s14))

# Test Case 8
s15 = "School master"
s16 = "The classroom"
print("Test Case 8: Are Anagrams?", are_anagrams(s15, s16))

# Test Case 9
s17 = "Dormitory"
s18 = "Dirty room"
print("Test Case 9: Are Anagrams?", are_anagrams(s17, s18))


'''
Output
Test Case 1: Are Anagrams? True
Test Case 2: Are Anagrams? True
Test Case 3: Are Anagrams? False
Test Case 4: Are Anagrams? False
Test Case 5: Are Anagrams? True
Test Case 6: Are Anagrams? True
Test Case 7: Are Anagrams? True
Test Case 8: Are Anagrams? True
Test Case 9: Are Anagrams? False'''


#**************************************************************************************************************************************

# 2. Problem Description: Binary Search

# You are tasked with creating a Python program to implement the binary search algorithm.
# Binary search is an efficient search algorithm that finds the position of a target value within a sorted array.
# The program should efficiently perform binary search and return the index of the target element if found, or -1 if the element is not present in the array.

# Input:
#    sorted_array: A sorted list of integers in ascending order.
#    target: The value to be searched in the array.

# Output:
#    Returns the index of the target element if found; otherwise, returns -1.

# Example:

# Example 1
# arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target1 = 6
# result1 = binary_search(arr1, target1)
# Output: 5

# Example 2
# arr2 = [2, 4, 6, 8, 10, 12, 14]
# target2 = 5
# result2 = binary_search(arr2, target2)
# Output: -1

# Example 3
# arr3 = [1, 3, 5, 7, 9, 11, 13]
# target3 = 1
# result3 = binary_search(arr3, target3)
# Output: 0

# Notes:
#        The function should return the correct index or -1 based on the binary search.


def binary_search(sorted_array, target):
    left = ?
    right = ?

    while left ?? right:
        mid = ? # do not use right + left / 2

        if sorted_array[?] ?? target:
            return ?
        elif sorted_array[mid] ? target:
            left = ??
        else:
            right = ??

    return ?


# Test cases

# Test Case 1
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target1 = 6
print("Test Case 1: Index of", target1, "=", binary_search(arr1, target1))

# Test Case 2
arr2 = [2, 4, 6, 8, 10, 12, 14]
target2 = 5
print("Test Case 2: Index of", target2, "=", binary_search(arr2, target2))

# Test Case 3
arr3 = [1, 3, 5, 7, 9, 11, 13]
target3 = 1
print("Test Case 3: Index of", target3, "=", binary_search(arr3, target3))

# Test Case 4
arr4 = [3, 6, 9, 12, 15, 18]
target4 = 15
print("Test Case 4: Index of", target4, "=", binary_search(arr4, target4))

# Test Case 5
arr5 = [5, 10, 15, 20, 25]
target5 = 8
print("Test Case 5: Index of", target5, "=", binary_search(arr5, target5))

'''
Output
Test Case 1: Index of 6 = 5
Test Case 2: Index of 5 = -1
Test Case 3: Index of 1 = 0
Test Case 4: Index of 15 = 4
Test Case 5: Index of 8 = -1
'''


#**************************************************************************************************************************************

# 3. Problem Description: Find the nth Fibonacci Number without Recursion

# You are tasked with creating a Python program to find the nth Fibonacci number without using recursion.
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
# The program should efficiently calculate and return the nth Fibonacci number.

# Input:
#     n: An integer representing the position in the Fibonacci sequence (n >= 0).
#
# Output:
#     Returns the nth Fibonacci number.

# Example:
# Example 1
# result1 = find_nth_fibonacci(5)
# Output: 5 (Fibonacci sequence: 0, 1, 1, 2, 3, 5)

# Example 2
# result2 = find_nth_fibonacci(8)
# Output: 21 (Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21)

# Example 3
# result3 = find_nth_fibonacci(10)
# Output: 55 (Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55)

# Notes:
#     The function should use an iterative approach without recursion.

def find_nth_fibonacci(n):
    if n < ?:
        raise ValueError("Input should be a non-negative integer.")

    if n == ?:
        return 0
    elif n == ?:
        return 1

    prev = ?
    current = ?

    for i in ?(?, n + 1):
        next_val = ? + ?
        prev = ?
        current = ?

    return ?



# Test Case 1

result1 = find_nth_fibonacci(5)
print("Test Case 1: Nth Fibonacci Number =", result1)

# Test Case 2
result2 = find_nth_fibonacci(8)
print("Test Case 2: Nth Fibonacci Number =", result2)

# Test Case 3
result3 = find_nth_fibonacci(10)
print("Test Case 3: Nth Fibonacci Number =", result3)

# Test Case 4
result4 = find_nth_fibonacci(0)
print("Test Case 4: Nth Fibonacci Number =", result4)

# Test Case 5
result5 = find_nth_fibonacci(2)
print("Test Case 5: Nth Fibonacci Number =", result5)

'''
Output
Test Case 1: Nth Fibonacci Number = 5
Test Case 2: Nth Fibonacci Number = 21
Test Case 3: Nth Fibonacci Number = 55
Test Case 4: Nth Fibonacci Number = 0
Test Case 5: Nth Fibonacci Number = 1
'''


#**************************************************************************************************************************************

# 4. Problem Description: Find the Next Prime Number

# You are tasked with creating a Python program to find the next prime number after a given number.
# The program should efficiently identify and return the next prime number that comes after the provided input.

# Input:
#     num: A positive integer greater than 1.

# Output:
#     Returns the next prime number greater than the input.

# Example 1
# result1 = findNextPrime(10)
# Output: 11 (The next prime number after 10 is 11)

# Example 2
# result2 = findNextPrime(20)
# Output: 23 (The next prime number after 20 is 23)

# Example 3
# result3 = findNextPrime(31)
# Output: 37 (The next prime number after 31 is 37)

# Notes:
#     The solution should efficiently find the next prime number after the given input.
#     The function should consider positive integers greater than 1 as input.
#     The program should run without errors for valid input values.

import math

def findNextPrime(num):
    if num < ?:
        raise ValueError("Input should be a positive integer greater than 1.")

    while True:
        ??

        if isPrime(?):
            return ?  

def isPrime(num):
    if num <= ?:
        return ?

    for i in ?(?, int(math.?(?)) + ?):
        if num ? i ?= ?:
            return False  

    return ?

# Test Case 1
input1 = 10
result1 = findNextPrime(input1)
print(f"Test Case 1: Next Prime Number = {result1}")

# Test Case 2
input2 = 20
result2 = findNextPrime(input2)
print(f"Test Case 2: Next Prime Number = {result2}")

# Test Case 3
input3 = 31
result3 = findNextPrime(input3)
print(f"Test Case 3: Next Prime Number = {result3}")

# Test Case 4
input4 = 1
try:
    result4 = findNextPrime(input4)
    print(f"Test Case 4: Next Prime Number = {result4}")
except ValueError as e:
    print(f"Test Case 4: {e}")


'''
Output:
Test Case 1: Next Prime Number = 11
Test Case 2: Next Prime Number = 23
Test Case 3: Next Prime Number = 37
Test Case 4: Next Prime Number = 2
'''


#**************************************************************************************************************************************

#5. Problem Description: Find Majority Element in an Array

# You are tasked with creating a Python program to find the majority element in an array.
# The majority element is defined as the element that appears more than n/2 times in the array, where n is the size of the array.
# The program should efficiently identify and return the majority element if it exists; otherwise, it should return -1.

# Input:
#     nums: An array of integers.

# Output:
#     Returns the majority element if it exists; otherwise, returns -1.

# Example:
# Example 1
# arr1 = [2, 2, 1, 1, 1, 2, 2]
# result1 = find_majority_element(arr1)
# Output: 2 (Majority element in the array is 2)

# Example 2
# arr2 = [3, 3, 4, 2, 4, 4, 2, 4, 4]
# result2 = find_majority_element(arr2)
# Output: 4 (Majority element in the array is 4)

# Example 3
# arr3 = [1, 2, 3, 4, 5]
# result3 = find_majority_element(arr3)
# Output: -1 (No majority element in the array)

def find_majority_element(nums):
    n = len(?)

    if n ?? 0:
        return -1  

    element_count = [0] ? 1001  

    for num in ?:
        element_count[?] ?? 1

    for i in range(len(?)):
        if element_count[?] > ???:
            return i 

    return -1  


# Test Case 1
arr1 = [2, 2, 1, 1, 1, 2, 2]
result1 = find_majority_element(arr1)
print("Test Case 1: Majority Element =", result1)

# Test Case 2
arr2 = [3, 3, 4, 2, 4, 4, 2, 4, 4]
result2 = find_majority_element(arr2)
print("Test Case 2: Majority Element =", result2)

# Test Case 3
arr3 = [1, 2, 3, 4, 5]
result3 = find_majority_element(arr3)
print("Test Case 3: Majority Element =", result3)

# Test Case 4
arr4 = [1, 1, 1, 2, 2]
result4 = find_majority_element(arr4)
print("Test Case 4: Majority Element =", result4)

# Test Case 5
arr5 = [5]
result5 = find_majority_element(arr5)
print("Test Case 5: Majority Element =", result5)

'''
Test Case 1: Majority Element = 2
Test Case 2: Majority Element = 4
Test Case 3: Majority Element = -1
Test Case 4: Majority Element = 1
Test Case 5: Majority Element = 5
'''


#**************************************************************************************************************************************

# 6. Problem Description: Calculate Character Frequency in a String

# You are tasked with creating a Python program to calculate the frequency of each character in a given string.
# The program should use a dictionary to store the frequency of each lowercase alphabet character (a to z) in the string.
# The output should display the frequency of each character.

# Input:
# input: A string containing lowercase alphabet characters.

# Output:
# Prints the frequency of each character in the format: "Character: Frequency".

# Example:
# String input = "abracadabra"
# calculate_char_frequency(input)
# Output:
# a: 5
# b: 2
# c: 1
# d: 1
# r: 2

# Notes:
# The solution should efficiently calculate the frequency of characters in the given string.
# The function should print the frequency for each lowercase alphabet character in the specified format.

def calculate_char_frequency(input_str):
    if ? input_str:
        print("Input string is empty.")
        return

    char_frequency = {}

    for char in ?:
        if ?.islower():
            char_frequency[?] = char_frequency.get(?, ?) + ?

    for char, frequency in char_frequency.items():
        print(f"{char}: {frequency}")


# Test Case 1
input1 = "abracadabra"
print("Test Case 1:")
calculate_char_frequency(input1)

# Test Case 2
input2 = "hello"
print("\nTest Case 2:")
calculate_char_frequency(input2)

# Test Case 3
input3 = "programming"
print("\nTest Case 3:")
calculate_char_frequency(input3)

# Test Case 4
input4 = "java"
print("\nTest Case 4:")
calculate_char_frequency(input4)

# Test Case 5
input5 = ""
print("\nTest Case 5:")
calculate_char_frequency(input5)

'''
Output:
Test Case 1:
a: 5
b: 2
c: 1
d: 1
r: 2

Test Case 2:
e: 1
h: 1
l: 2
o: 1

Test Case 3:
a: 1
g: 2
i: 1
m: 2
n: 1
o: 1
p: 1
r: 2

Test Case 4:
a: 2
j: 1
v: 1

Test Case 5:
Input string is empty.
'''


#**************************************************************************************************************************************

# 7. Problem Description: Find the Sum of Two Largest Elements in an Array

# You are tasked with creating a Python program to find the sum of the two largest elements in an array.
# The program should efficiently calculate and return the sum of the two largest distinct elements in the array.

# Input:
#     nums: An array of integers.

# Output:
#     Returns the sum of the two largest distinct elements in the array.

# Example 1
# arr1 = [3, 7, 2, 8, 5]
# result1 = sum_of_two_largest(arr1)
# Output: 15 (The two largest elements are 8 and 7, and their sum is 15)

# Example 2
# arr2 = [5, 5, 5, 5]
# result2 = sum_of_two_largest(arr2)
# Output: 10 (The two largest distinct elements are both 5, and their sum is 10)

# Notes:
#     The solution should efficiently find and calculate the sum of the two largest distinct elements in the array.
#     The function should consider arrays of varying sizes and handle cases where there are not enough distinct elements.
#     The program should run without errors for valid input arrays.

def sum_of_two_largest(nums):
    if nums is None or len(?) < 2:
        raise ValueError("Array should contain at least two elements.")

    first_largest = float('-inf')
    second_largest = float('-inf')

    ? num in ?:
        if num > first_largest:
            second_largest = ?
            first_largest = ?
        elif num ? second_largest ? num < ?:
            second_largest = ??

    if second_largest ?? float('-inf'):
        raise ValueError("Array should contain at least two distinct elements.")

    return ? + ?

# Test Cases
# Test Case 1
arr1 = [3, 7, 2, 8, 5]
result1 = sum_of_two_largest(arr1)
print("Test Case 1: Sum of Two Largest =", result1)

# Test Case 2
arr2 = [5, 8, 4, 3]
result2 = sum_of_two_largest(arr2)
print("Test Case 2: Sum of Two Largest =", result2)

# Test Case 3
arr3 = [1, 2, 3, 4, 5]
result3 = sum_of_two_largest(arr3)
print("Test Case 3: Sum of Two Largest =", result3)

# Test Case 4
arr4 = [10, 10, 20, 20, 30]
result4 = sum_of_two_largest(arr4)
print("Test Case 4: Sum of Two Largest =", result4)

# Test Case 5
arr5 = [5, 3]
result5 = sum_of_two_largest(arr5)
print("Test Case 5: Sum of Two Largest =", result5)

'''
Output:
Test Case 1: Sum of Two Largest = 15
Test Case 2: Sum of Two Largest = 13
Test Case 3: Sum of Two Largest = 9
Test Case 4: Sum of Two Largest = 50
Test Case 5: Sum of Two Largest = 8
'''




#**************************************************************************************************************************************

# 8. Problem Description: Square of the Sum of Digits

# You are tasked with creating a Python program to find the square of the sum of digits of a given number.
# The program should efficiently calculate and return the square of the sum of the individual digits of the input number.

# Input:
#     num: A non-negative integer.

# Output:
#     Returns the square of the sum of the individual digits of the input number.

# Example 1
# result1 = square_of_sum_of_digits(123)
# Output: 36 (The sum of digits is 1 + 2 + 3 = 6, and the square of 6 is 36)

# Example 2
# result2 = square_of_sum_of_digits(456)
# Output: 81 (The sum of digits is 4 + 5 + 6 = 15, and the square of 15 is 225)

# Notes:
#     The solution should efficiently calculate the square of the sum of digits for a given non-negative integer.
#     The function should handle valid non-negative integer inputs.
#     The program should run without errors for valid input numbers.

def square_of_sum_of_digits(num):
    if num < ?:
        raise ValueError("Input should be a non-negative integer.")

    sum_of_digits = ?

    while num ? 0:
        digit = num ? ?
        sum_of_digits ?? digit
        num ??? 10

    square_of_sum = ???
    return ?

# Test Cases
# Test Case 1
input1 = 123
result1 = square_of_sum_of_digits(input1)
print("Test Case 1: Square of Sum of Digits =", result1)

# Test Case 2
input2 = 456
result2 = square_of_sum_of_digits(input2)
print("Test Case 2: Square of Sum of Digits =", result2)

# Test Case 3
input3 = 7890
result3 = square_of_sum_of_digits(input3)
print("Test Case 3: Square of Sum of Digits =", result3)

# Test Case 4
input4 = 0
result4 = square_of_sum_of_digits(input4)
print("Test Case 4: Square of Sum of Digits =", result4)

# Test Case 5
input5 = 987654321
result5 = square_of_sum_of_digits(input5)
print("Test Case 5: Square of Sum of Digits =", result5)

'''
Output:
Test Case 1: Square of Sum of Digits = 36
Test Case 2: Square of Sum of Digits = 225
Test Case 3: Square of Sum of Digits = 576
Test Case 4: Square of Sum of Digits = 0
Test Case 5: Square of Sum of Digits = 2025
'''



#**************************************************************************************************************************************

# 9. Problem Description: Check if a Number is a Perfect Square

# You are tasked with creating a Python program to determine whether a given number is a perfect square.
# The program should efficiently check and return True if the number is a perfect square, and False otherwise.

# Input:
#     num: A non-negative integer.

# Output:
#     Returns True if the number is a perfect square, and False otherwise.

# Example 1
# result1 = isPerfectSquare(16)
# Output: True (16 is a perfect square, as 4 * 4 = 16)

# Example 2
# result2 = isPerfectSquare(25)
# Output: True (25 is a perfect square, as 5 * 5 = 25)

# Example 3
# result3 = isPerfectSquare(14)
# Output: False (14 is not a perfect square)

# Notes:
#     The solution should efficiently check whether the given number is a perfect square.
#     The function should handle non-negative integers as input.
#     The program should run without errors for valid input numbers.

def isPerfectSquare(num):
    if num < ?:
        raise ValueError("Input should be a non-negative integer.")

    sqrt_root = ?

    while ? * ? <= num:
        if ? ? ? == num:
            return True  
        sqrt_root ?? 1

    return ?  

# Test Cases
input1 = 16
result1 = isPerfectSquare(input1)
print("Test Case 1: Is Perfect Square?", result1)

input2 = 25
result2 = isPerfectSquare(input2)
print("Test Case 2: Is Perfect Square?", result2)

input3 = 14
result3 = isPerfectSquare(input3)
print("Test Case 3: Is Perfect Square?", result3)

input4 = 0
result4 = isPerfectSquare(input4)
print("Test Case 4: Is Perfect Square?", result4)

input5 = 100
result5 = isPerfectSquare(input5)
print("Test Case 5: Is Perfect Square?", result5)

'''
Sample Output:
Test Case 1: Is Perfect Square? True
Test Cae 3: Is Perfect Square? False
Test Casese 2: Is Perfect Square? True
Test Cas 4: Is Perfect Square? True
Test Case 5: Is Perfect Square? True
'''



#**************************************************************************************************************************************

#10. Problem Description: Difference Between Sum of Even and Odd-Indexed Elements

# You are tasked with creating a Python program to find the difference between the sum of even-indexed elements and odd-indexed elements in an array.
# The program efficiently calculates and returns the absolute difference between the sums of elements at even and odd indices in the array.

# Input:
#     nums: An array of integers.

# Output:
#     Returns the absolute difference between the sum of even-indexed elements and odd-indexed elements in the array.

# Example 1
# arr1 = [1, 2, 3, 4, 5]
# result1 = difference_between_sums(arr1)
# Output: 3 (Sum of even-indexed elements: 1 + 3 + 5 = 9, Sum of odd-indexed elements: 2 + 4 = 6, Difference = |9 - 6| = 3)

# Example 2
# arr2 = [10, 20, 30, 40, 50, 60]
# result2 = difference_between_sums(arr2)
# Output: 30 (Sum of even-indexed elements: 10 + 30 + 50 = 90, Sum of odd-indexed elements: 20 + 40 + 60 = 120, Difference = |90 - 120| = 30)

# Notes:
#     The solution should efficiently find and calculate the difference between the sum of even-indexed elements and odd-indexed elements in the array.
#     The function should consider arrays of varying sizes and handle cases where the array may not have both even and odd indices.
#     The program should run without errors for valid input arrays.


def difference_between_sums(nums):
    if ? is None or len(?) < 2:
        raise ValueError("Array should contain at least two elements.")

    sum_even = ?(nums[::?]) # use slicing 
    sum_odd = ?(nums[?::?])

    return abs(? ? ?)

def main():
    # Test Case 1
    arr1 = [1, 2, 3, 4, 5]
    result1 = difference_between_sums(arr1)
    print("Test Case 1: Difference Between Sums =", result1)

    # Test Case 2
    arr2 = [10, 20, 30, 40, 50, 60]
    result2 = difference_between_sums(arr2)
    print("Test Case 2: Difference Between Sums =", result2)

    # Test Case 3
    arr3 = [5]
    try:
        result3 = difference_between_sums(arr3)
        print("Test Case 3: Difference Between Sums =", result3)
    except ValueError as e:
        print("Test Case 3:", e)

    # Test Case 4
    arr4 = [2, 4]
    result4 = difference_between_sums(arr4)
    print("Test Case 4: Difference Between Sums =", result4)

    # Test Case 5
    arr5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result5 = difference_between_sums(arr5)
    print("Test Case 5: Difference Between Sums =", result5)

# Execute the main method
if __name__ == "__main__":
    main()

'''
Output:
Test Case 1: Difference Between Sums = 3
Test Case 2: Difference Between Sums = 30
Test Case 3: Array should contain at least two elements.
Test Case 4: Difference Between Sums = 2
Test Case 5: Difference Between Sums = 5
'''


#**************************************************************************************************************************************

# 11. Armstrong Number
#
# You are tasked with creating a python program to determine whether a given integer 'n' is an Armstrong number.
# An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits in the number.

# Input:
#    n: An integer representing the number to be checked for being an Armstrong number.

# Output:
#    Returns true if the input number n is an Armstrong number, and false otherwise.

# Example 1
#Input: 153
#Output: true
#Explanation: 1^3 + 5^3 + 3^3 = 153

# Example 2
#Input: 370
#Output: true
#Explanation: 3^3 + 7^3 + 0^3 = 370

# Example 3
#Input: 9474
#Output: true
#Explanation: 9^4 + 4^4 + 7^4 + 4^4 = 9474

# Example 4
#Input: 123
#Output: false
#Explanation: 1^3 + 2^3 + 3^3 ≠ 123

# Notes:
#        The solution should efficiently determine whether the input number is an Armstrong number.
#        Armstrong numbers are positive integers with at least two digits.
#        The program should run without errors for valid input values.

class ArmstrongNumber:

    @staticmethod
    def is_armstrong(n):
        # Count the number of digits in the number
        num_digits = len(str(?))
        temp = ?
        
        sum_of_powers = ?(int(digit) ?? num_digits for digit ? str(?))
        
        return sum_of_powers ?? n

    @staticmethod
    def main():
        # Test Cases
        print("Test Case 1:")
        n1 = 153
        print("Input:", n1)
        print("Output:", ArmstrongNumber.is_armstrong(n1))

        print("\nTest Case 2:")
        n2 = 370
        print("Input:", n2)
        print("Output:", ArmstrongNumber.is_armstrong(n2))

        print("\nTest Case 3:")
        n3 = 9474
        print("Input:", n3)
        print("Output:", ArmstrongNumber.is_armstrong(n3))

        print("\nTest Case 4:")
        n4 = 123
        print("Input:", n4)
        print("Output:", ArmstrongNumber.is_armstrong(n4))


# Execute the main method
if __name__ == "__main__":
    ArmstrongNumber.main()

'''
Output:
Test Case 1:
Input: 153
Output: True

Test Case 2:
Input: 370
Output: True

Test Case 3:
Input: 9474
Output: True

Test Case 4:
Input: 123
Output: False
'''



#**************************************************************************************************************************************

# 12.  Count Unique Characters in a String
#
# You are tasked with writing a Python program to count the number of unique characters in a given string.
# The uniqueness of characters should be case insensitive, meaning uppercase and lowercase characters should be treated as the same.
# Input:
#    str: A string containing characters.
#
# Output:
#    Returns an integer representing the count of unique characters in the input string str.
#
# Example 1
#Input: "Hello"
#Output: 3  // 'H', 'e', 'o'
#
#Example 2
#Input: "Mississippi"
#Output: 1  // 'M'
#
#Example 3
#Input: "JavaProgramming"
#Output: 6  // 'J', 'v', 'P', 'o', 'g', 'i'
#
# Notes:
#    The input string may contain alphanumeric characters and special symbols.
#    The program should consider characters case-insensitively. For example, 'a' and 'A' should be considered the same character.
#    The program should efficiently determine the count of unique characters in the string.

class UniqueCharacterCounter:

    @staticmethod
    def count_unique_characters(string):
        
        frequency = {}
        string = string.?()  # Convert the string to lowercase

        
        for ch in ?:
            if ?.isalpha():
                frequency[?] = frequency.get(?, ?) + ?

     
        unique_count = ?(1 for freq in ?.values() if freq == ?)

        return ?

    @staticmethod
    def main():
        # Test Cases
        test_cases = ["Hello", "Mississippi", "JavaProgramming"]
        for idx, test_case in enumerate(test_cases, start=1):
            print(f"Test Case {idx}:")
            print("Input:", test_case)
            print("Output:", UniqueCharacterCounter.count_unique_characters(test_case))

# Execute the main method
if __name__ == "__main__":
    UniqueCharacterCounter.main()

'''
Output:
Test Case 1:
Input: Hello
Output: 3
Test Case 2:
Input: Mississippi
Output: 1
Test Case 3:
Input: JavaProgramming
Output: 6
'''



#**************************************************************************************************************************************

# 13. Peak Element in Array
#
# You are given an array of integers.
# A peak element in the array is an element that is strictly greater than its neighbors.
# It is the largest element in the array, satisfying the given condition. Additionally, it's important to note that there are no duplicates in the array.
#
# Input:
#    nums: An array of integers.
#
# Output:
#    Returns the peak element in the array.
#
# Example 1
#Input: nums = [5, 10, 20, 15]
#Output: 20
#Explanation: The element 20 is strictly greater than its neighbors 10 and 15.
#
# Example 2
#Input: nums = [1, 3, 6, 7, 4, 2]
#Output: 7
#Explanation: The element 7 is strictly greater than its neighbors 6 and 4.
#
# Example 3
#Input: nums = [10, 20, 30, 40]
#Output: 40
#Explanation: The element 40 is strictly greater than its neighbor 30.
#
# Example 4
#Input: nums = [5, 10, 15, 20, 25]
#Output: 25
#Explanation: The element 25 is strictly greater than its neighbor 20.
#
# Notes:
#    The array will contain at least one element.
#    There will be exactly one peak element in the array.
#    The peak element is guaranteed to be greater than its adjacent elements.
#    Use linear search approach to find the peak element efficiently.

class PeakElement:

    @staticmethod
    def find_peak_element(nums):
        n = len(?) 

        # Edge cases
        if n == ?:
            return nums[0]

        # Check first element
        if nums[?] > nums[?]:
            return nums[?]

        # Check last element
        if nums[??] > nums[??]:
            return nums[??]

        # Check middle elements
        for i in range(1, ??):
            if nums[i] > nums[??] ? nums[i] > nums[??]:
                return nums[?]

        return -1  # Peak element not found

    @staticmethod
    def main():
        # Test Cases
        nums1 = [5, 10, 20, 15]
        print("Test Case 1:", PeakElement.find_peak_element(nums1))  # Output: 20

        nums2 = [1, 3, 6, 7, 4, 2]
        print("Test Case 2:", PeakElement.find_peak_element(nums2))  # Output: 7

        nums3 = [10, 20, 30, 40]
        print("Test Case 3:", PeakElement.find_peak_element(nums3))  # Output: 40

        nums4 = [5, 10, 15, 20, 25]
        print("Test Case 4:", PeakElement.find_peak_element(nums4))  # Output: 25

        nums5 = [1]
        print("Test Case 5:", PeakElement.find_peak_element(nums5))  # Output: 1

        nums6 = [10, 9, 8, 7]
        print("Test Case 6:", PeakElement.find_peak_element(nums6))  # Output: 10

        nums7 = [10, 11, 13, 16, 20, 8, 5, 4]
        print("Test Case 7:", PeakElement.find_peak_element(nums7))  # Output: 20

        nums8 = [20, 40, 50, 70, 90, 60, 30, 10]
        print("Test Case 8:", PeakElement.find_peak_element(nums8))  # Output: 90

# Execute the main method
if __name__ == "__main__":
    PeakElement.main()

'''
Output:
Test Case 1: 20
Test Case 2: 7
Test Case 3: 40
Test Case 4: 25
Test Case 5: 1
Test Case 6: 10
Test Case 7: 20
Test Case 8: 90
'''



#**************************************************************************************************************************************

# 14. Leap Year Checker

# You are tasked with creating a Java program to determine whether a given year is a leap year or not.
# A leap year is a year that is evenly divisible by 4, except for years that are evenly divisible by 100.
# However, years that are evenly divisible by 400 are leap years.

# Input:
#     year: An integer representing the year to be checked.

# Output:
#     Returns true if the input year is a leap year, and false otherwise.

# Example 1
# Input: year = 2020
# Output: true
# Explanation: 2020 is divisible by 4 and not divisible by 100, so it's a leap year.

# Example 2
# Input: year = 1900
# Output: false
# Explanation: Although 1900 is divisible by 4, it is also divisible by 100.
# Since it's not divisible by 400, it's not a leap year.

# Example 3
# Input: year = 2000
# Output: true
# Explanation: 2000 is divisible by 4, divisible by 100, and divisible by 400,
# making it a leap year.

# Example 4
# Input: year = 2021
# Output: false
# Explanation: 2021 is not divisible by 4, so it's not a leap year.

# Notes:
#     The input year is a positive integer.
#     Implement the logic to check whether the given year is a leap year or not.
#     The program should return true if the year is a leap year, and false otherwise.

def is_leap_year(year):
    if (year ? 4 ?= ? ?? year % 100 ?? 0) ? (year % ? ?= 0):
        return ? 
    else:
        return False 

# Test Cases
years = [2020, 1900, 2000, 2021, 2022, 3036, 3033, 1986, 1956, 1600]
for year in years:
    print(f"Is {year} a leap year? {is_leap_year(year)}")

'''
Output:
Is 2020 a leap year? True
Is 1900 a leap year? False
Is 2000 a leap year? True
Is 2021 a leap year? False
Is 2022 a leap year? False
Is 3036 a leap year? True
Is 3033 a leap year? False
Is 1986 a leap year? False
Is 1956 a leap year? True
Is 1600 a leap year? True
'''

#**************************************************************************************************************************************

# 15. Problem Description: Check if a String Starts with a Specific Prefix
#
# You are tasked with creating a Python program to check if a given string starts with a specific prefix.
# The program should efficiently determine and return True if the string begins with the specified prefix, and False otherwise.

# Input:
#    str: A string.
#    prefix: The prefix to check.

# Output:
#    Returns True if the string starts with the specified prefix, and False otherwise.

# Example 1
# result1 = starts_with_prefix("Hello, World!", "Hello")
# Output: True ("Hello, World!" starts with the prefix "Hello")

# Example 2
# result2 = starts_with_prefix("Java Programming", "Python")
# Output: False ("Java Programming" does not start with the prefix "Python")

# Example 3
# result3 = starts_with_prefix("12345", "12")
# Output: True ("12345" starts with the prefix "12")

# Notes:
#    The solution should efficiently check whether the given string starts with the specified prefix.
#    The function should handle cases where the string or prefix may be empty.
#    The program should run without errors for valid input strings and prefixes.

def starts_with_prefix(string, prefix):
    if ? is None or ? is None:
        raise ValueError("Input strings cannot be None.")

    prefix_length = len(?)

    if prefix_length > len(?):
        return ?  

    for i in ?(?):
        if ?[?] != ?[?]:
            return ?  

    return True  

# Test Case 1
result1 = starts_with_prefix("Hello, World!", "Hello")
print("Test Case 1: Starts with Prefix?", result1)

# Test Case 2
result2 = starts_with_prefix("Java Programming", "Python")
print("Test Case 2: Starts with Prefix?", result2)

# Test Case 3
result3 = starts_with_prefix("12345", "12")
print("Test Case 3: Starts with Prefix?", result3)

# Test Case 4
result4 = starts_with_prefix("Java", "Java")
print("Test Case 4: Starts with Prefix?", result4)

# Test Case 5
result5 = starts_with_prefix("", "Prefix")
print("Test Case 5: Starts with Prefix?", result5)


'''
Output:
Test Case 1: Starts with Prefix? True
Test Case 2: Starts with Prefix? False
Test Case 3: Starts with Prefix? True
Test Case 4: Starts with Prefix? True
Test Case 5: Starts with Prefix? False
'''



#**************************************************************************************************************************************

# 16. Pairs with Sum

# You are tasked with creating a Python program to find all pairs of elements in an array whose sum is equal to a given target number.

# Input:
#    nums: An array of integers representing the input array.
#    target: An integer representing the target sum.

# Output:
#    Prints all pairs of elements in the array nums whose sum equals the target.

# Example 1
#Input: nums = {1, 2, 3, 4, 5}, target = 5
#Output: (1, 4), (2, 3)
#Explanation: In the input array, the pairs (1, 4) and (2, 3) have a sum equal to the target 5.

# Example 2
#Input: nums = {3, 8, 5, 2, 9}, target = 10
#Output: (3, 7), (8, 2)
#Explanation: In the input array, the pairs (3, 7) and (8, 2) have a sum equal to the target 10.

# Notes:
#    Each pair should be printed only once, and the order of elements within the pair does not matter.
#    If there are no such pairs in the array whose sum equals the target, print "No pairs found."

class PairSum:

    @staticmethod
    def find_pairs(nums, target):
        found_pair = False
        # Brute-force approach: Check all pairs of elements in the array
        for i in range(??):
            for j in range(??, ??):
                if nums[?] + nums[?] ?= ?:
                    print("({}, {})".format(nums[i], nums[j]))
                    found_pair = ?
        if not ?:
            print("No pairs found.")

    @staticmethod
    def main():
        # Test Cases
        nums1 = [1, 2, 3, 4, 5]
        target1 = 5
        print("Pairs with sum {} in nums1:".format(target1))
        PairSum.find_pairs(nums1, target1)

        nums2 = [3, 8, 5, 2, 9]
        target2 = 10
        print("\nPairs with sum {} in nums2:".format(target2))
        PairSum.find_pairs(nums2, target2)

        nums3 = [1, 2, 3, 4, 5]
        target3 = 20
        print("\nPairs with sum {} in nums3:".format(target3))
        PairSum.find_pairs(nums3, target3)

        nums4 = [5, 4, 6, 5]
        target4 = 10
        print("\nPairs with sum {} in nums4:".format(target4))
        PairSum.find_pairs(nums4, target4)

        nums5 = [1, 2, 3, 4, 5]
        target5 = 8
        print("\nPairs with sum {} in nums5:".format(target5))
        PairSum.find_pairs(nums5, target5)

# Execute the main method
if __name__ == "__main__":
    PairSum.main()

'''
Output:
Pairs with sum 5 in nums1:
(1, 4)
(2, 3)

Pairs with sum 10 in nums2:
(8, 2)

Pairs with sum 20 in nums3:
No pairs found.

Pairs with sum 10 in nums4:
(5, 5)
(4, 6)

Pairs with sum 8 in nums5:
(3, 5)
'''



#**************************************************************************************************************************************

# 17. Swap numbers

# In this problem, you are given two integer variables a and b.
# The task is to swap the values of these variables without using an additional third variable.
# This means that after the swapping operation, the value of a should be replaced with the original value of b, and vice versa, without using any extra storage.
#
# The goal is to implement a method swap that performs this swapping operation efficiently,
# ensuring that the original values of a and b are modified accordingly.
#
# Test cases are provided to validate the correctness of the swapping operation,
# covering different scenarios such as positive and negative integers, as well as zero.
# The method should be able to handle these cases and produce the correct swapped values for a and b.

def swap(a, b):
    print("Before swapping:")
    print("a =", a)
    print("b =", b)

    # Swapping without using a third variable
    ????
    ????
    ????

    print("After swapping:")
    print("a =", a)
    print("b =", b)

# Test Cases
num1, num2 = 5, 10
print("Swapping num1 and num2:")
swap(num1, num2)

num3, num4 = 3, 7
print("\nSwapping num3 and num4:")
swap(num3, num4)

num5, num6 = 20, 50
print("\nSwapping num5 and num6:")
swap(num5, num6)

num7, num8 = 1, 4
print("\nSwapping num7 and num8:")
swap(num7, num8)

num9, num10 = 15, 25
print("\nSwapping num9 and num10:")
swap(num9, num10)

'''
Output:
Swapping num1 and num2:
Before swapping:
a = 5
b = 10
After swapping:
a = 10
b = 5

Swapping num3 and num4:
Before swapping:
a = 3
b = 7
After swapping:
a = 7
b = 3

Swapping num5 and num6:
Before swapping:
a = 20
b = 50
After swapping:
a = 50
b = 20

Swapping num7 and num8:
Before swapping:
a = 1
b = 4
After swapping:
a = 4
b = 1

Swapping num9 and num10:
Before swapping:
a = 15
b = 25
After swapping:
a = 25
b = 15
'''





#**************************************************************************************************************************************

# 18. Finding Factors
#
# You are tasked with creating a Python program to find all the factors (numbers that evenly divide) of a given input number.
#
# Input:
#     n: A positive integer representing the input number.
#
# Output:
#     Prints all the factors of the input number n.
#
# Example 1
# Input: n = 12
# Output: Factors of 12: 1, 2, 3, 4, 6, 12
# Explanation: The factors of 12 are 1, 2, 3, 4, 6, and 12.
#
# Example 2
# Input: n = 15
# Output: Factors of 15: 1, 3, 5, 15
# Explanation: The factors of 15 are 1, 3, 5, and 15.
#
# Notes:
#     Factors are the numbers that divide the given input number evenly without leaving a remainder.
#     The factors should be printed in ascending order.
#     Include the input number itself and 1 as factors.

class Factors:

    @staticmethod
    def find_factors(n):
        print("Factors of", n, end=": ")
        # Iterate from 1 to n and check if i divides n evenly
        factors = []
        for i in range(?, ??):
            if n ? i ?= ?:
                ?.append(?)
        print(", ".join(map(str, ?)))

    @staticmethod
    def main():
        # Test Cases
        num1 = 12
        print("Test Case 1:")
        Factors.find_factors(num1)

        num2 = 15
        print("\nTest Case 2:")
        Factors.find_factors(num2)

        num3 = 28
        print("\nTest Case 3:")
        Factors.find_factors(num3)

# Execute the main method
if __name__ == "__main__":
    Factors.main()

'''
Output;
Test Case 1:
Factors of 12: 1, 2, 3, 4, 6, 12

Test Case 2:
Factors of 15: 1, 3, 5, 15

Test Case 3:
Factors of 28: 1, 2, 4, 7, 14, 28
'''


#**************************************************************************************************************************************
# 19. Problem Description: Sum of Prime Numbers up to a Given Limit
#
# You are tasked with creating a Python program to find the sum of prime numbers up to a given limit.
# The program should efficiently determine and return the sum of all prime numbers within the specified range.
#
# Function Signature: def sum_of_primes(limit: int) -> int
#
# Input:
#     limit: An integer representing the upper limit of the range.
#
# Output:
#     Returns the sum of prime numbers up to the given limit.
#
# Example
# result = sum_of_primes(10)
# Output: 17 (2 + 3 + 5 + 7 are prime numbers up to the limit 10)
#
# Notes:
#     The solution should efficiently find and return the sum of prime numbers up to the specified limit.
#     The function should handle non-negative integer inputs.
#     The program should run without errors for valid input limits.


import math

class SumOfPrimes:
   
    def sum_of_primes(limit):
        if limit < ?:
            raise ValueError("Limit should be a non-negative integer.")

        prime_sum = ?

        for i in range(?, ??):
            if SumOfPrimes.is_prime(?):
                prime_sum ?? i

        return ?
    
    def is_prime(num):
        if num < ?:
            return False

        for i in ?(?, int(math.?(?)) + ?):
            if num ? i ?= ?:
                return False  

        return ?  


# Test Case 1
result1 = SumOfPrimes.sum_of_primes(10)
print("Test Case 1: Sum of Primes =", result1)

# Test Case 2
result2 = SumOfPrimes.sum_of_primes(20)
print("Test Case 2: Sum of Primes =", result2)

# Test Case 3
result3 = SumOfPrimes.sum_of_primes(5)
print("Test Case 3: Sum of Primes =", result3)

# Test Case 4
result4 = SumOfPrimes.sum_of_primes(0)
print("Test Case 4: Sum of Primes =", result4)

# Test Case 5
result5 = SumOfPrimes.sum_of_primes(30)
print("Test Case 5: Sum of Primes =", result5)

'''
Sample Output:
Test Case 1: Sum of Primes = 17
Test Case 2: Sum of Primes = 77
Test Case 3: Sum of Primes = 10
Test Case 4: Sum of Primes = 0
Test Case 5: Sum of Primes = 129
'''



#**************************************************************************************************************************************
#  20. Problem Description: Find the Kth Largest Element in an Array

#You are tasked with creating a Python program to find the Kth largest element in an array.
# The program should efficiently determine and return the Kth largest element from the given array.

#Input:
#    nums: A list of integers.
#    k: An integer representing the position of the Kth largest element (1 <= k <= length of the array).

#Output:
#    Returns the Kth largest element from the array.

# Example
#arr = [3, 1, 5, 7, 2, 4, 6]
#k = 3
#result = findKthLargest(arr, k)
# Output: 5 (The 3rd largest element in the array is 5)

#Notes:
#    The solution should efficiently find and return the Kth largest element from the array.
#    The function should handle valid positions for K within the range of the array length.
#    The program should run without errors for valid input arrays and positions.

class KthLargestElement:

    @staticmethod
    def findKthLargest(nums, k):
        if nums is None or k ?= 0 ?? k ? len(?):
            raise ValueError("Invalid input parameters.")

        ????
        return ????

    @staticmethod
    def main():
        # Test Case 1
        arr1 = [3, 1, 5, 7, 2, 4, 6]
        k1 = 3
        result1 = KthLargestElement.findKthLargest(arr1, k1)
        print("Test Case 1: Kth Largest Element =", result1)

        # Test Case 2
        arr2 = [10, 20, 30, 40, 50]
        k2 = 1
        result2 = KthLargestElement.findKthLargest(arr2, k2)
        print("Test Case 2: Kth Largest Element =", result2)

        # Test Case 3
        arr3 = [7]
        k3 = 1
        result3 = KthLargestElement.findKthLargest(arr3, k3)
        print("Test Case 3: Kth Largest Element =", result3)

        # Test Case 4
        arr4 = [5, 5, 5, 5, 5]
        k4 = 2
        result4 = KthLargestElement.findKthLargest(arr4, k4)
        print("Test Case 4: Kth Largest Element =", result4)

        # Test Case 5
        arr5 = [1, 2, 3, 4, 5]
        k5 = 5
        result5 = KthLargestElement.findKthLargest(arr5, k5)
        print("Test Case 5: Kth Largest Element =", result5)

KthLargestElement.main()

'''
#Sample Output:
Test Case 1: Kth Largest Element = 5
Test Case 2: Kth Largest Element = 50
Test Case 3: Kth Largest Element = 7
Test Case 4: Kth Largest Element = 5
Test Case 5: Kth Largest Element = 1
'''


#**************************************************************************************************************************************
# 21. Problem Description: Single Number
# You are tasked with creating a Python program to find the single number in an array where every element appears twice except for one.
# Your solution must have linear runtime complexity and use only constant extra space.

# Input:
#     nums: A non-empty array of integers where every element appears twice except for one.

# Output:
#     Returns the single number that appears only once in the array.

# Example
# arr = [4, 2, 7, 2, 4]
# result = findSingleNumber(arr)
# Output: 7 (7 is the only element that appears once in the array)

# Notes:
#     The solution should have linear runtime complexity O(n) and use only constant extra space O(1).
#     The array will always contain an odd number of elements.
#     The program should run without errors for valid input arrays.

def findSingleNumber(nums):
    if nums is None or len(?) ? 2 ?= 0:
        raise ValueError("Invalid input array.")

    result = ?

    for num in ?:
        result ??? ?  

    return ?

# Test Case 1
arr1 = [4, 2, 7, 2, 4]
result1 = findSingleNumber(arr1)
print("Test Case 1: Single Number =", result1)

# Test Case 2
arr2 = [1, 2, 3, 1, 3]
result2 = findSingleNumber(arr2)
print("Test Case 2: Single Number =", result2)

# Test Case 3
arr3 = [5, 6, 6]
result3 = findSingleNumber(arr3)
print("Test Case 3: Single Number =", result3)

'''
Output:
Test Case 1: Single Number = 7
Test Case 2: Single Number = 2
Test Case 3: Single Number = 5
'''



#**************************************************************************************************************************************
#  22. Problem Description: Missing Number

# You are tasked with creating a Python program to find the missing number in an array.
# Given an array nums containing n distinct numbers in the range [0, n],
# the program should efficiently determine and return the only number in the range that is missing from the array.

# Input:
#     nums: An array of distinct integers in the range [0, n], where n is the length of the array.

# Output:
#     Returns the missing number from the array.

# Example
# arr = [3, 0, 1]
# result = find_missing_number(arr)
# Output: 2 (The missing number in the array is 2)

# Notes:
#     The solution should efficiently find and return the missing number in the array.
#     The array will always contain n distinct numbers in the range [0, n], where n is the length of the array.
#     The program should run without errors for valid input arrays.


def find_missing_number(nums):
    if nums is None or len(?) == ?:
        raise ValueError("Invalid input array.")

    n = len(?)
    expected_sum = ?
    actual_sum = ?

    return ? - ?


# Test cases
# Test Case 1
arr1 = [3, 0, 1]
result1 = find_missing_number(arr1)
print("Test Case 1: Missing Number =", result1)

# Test Case 2
arr2 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
result2 = find_missing_number(arr2)
print("Test Case 2: Missing Number =", result2)

# Test Case 3
arr3 = [1]
result3 = find_missing_number(arr3)
print("Test Case 3: Missing Number =", result3)

# Sample Output:
# Test Case 1: Missing Number = 2
# Test Case 2: Missing Number = 8
# Test Case 3: Missing Number = 0