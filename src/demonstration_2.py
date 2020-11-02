"""
You are given a non-empty array that represents the digits of a non-negative integer.

Write a function that increments the number by 1.

The digits are stored so that the digit representing the most significant place value is at the beginning of the array. Each element in the array only contains a single digit.

You will not receive a leading 0 in your input array (except for the number 0 itself).

Example 1:

Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.

Example 2:

Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.

Example 3:

Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""
from typing import List

def plus_one(digits):
    #digits: List[int] --> List[int]
    # Your code here
    #given a list of single-digit numbers that together represent
    #a single number
    #increment the number by 1
    #change 9 to 0 & increment the digit to the left by 1
    #this might cascade if we have more than one 9 to the left
    #if all the digits are 9s, then we need to add an additional digit to the left
    for i in range(len(digits) - 1, -1, -1):
    #the last digit up to & including 0
    #3rd param the step --> we want to go backwards
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] +=1
            return digits

    return [1] + digits
    #or return digits.insert(0,1)

print (plus_one([1,3,2]))
print (plus_one([3,2,1,9]))
print (plus_one([1,9,9]))
print (plus_one([9,9,9]))
