#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 23 :

# Write a method which can calculate square value of number

# Hints:
# Using the ** operator

def main(num):
    return num ** 2

if __name__ == "__main__":
    num = int(input("Enter the number : "))
    print(main(num))