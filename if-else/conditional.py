import random

def is_positive(num):
    # return true if num is positive, otherwise return false
    return num>=0

def is_even(num):
    # return true if num is even, otherwise return false
    return num%2==0

def is_positive_and_even(num):
    # return true if num is positive and even, otherwise return false
    return num>0 && num%2==0

def is_positive_or_even(num):
    # return true if num is positive or even, otherwise return false
    return num>0 || num%2==0
