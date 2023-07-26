#!/usr/bin/python3

def factorise(natural_number):
    int_natural_number = int(natural_number ** 0.5) + 1
    for i in range(2, int_natural_number):
        if natural_number % i != 0:
            return natural_number, 1
        elif natural_number % i == 0:
            return i, number // i

