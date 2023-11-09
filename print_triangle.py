#!/usr/bin/env python3
import sys

def print_triangle(char: str, height: int) -> None:
    """
    Print a triangle of a given height using the provided character.
    
    Parameters:
    - char (str): The character to print.
    - height (int): The number of characters tall the triangle should be.
    """
    if height%2 == 0:
        for i in range(1,height//2+1):
            print(i*char)
        for i in range(height//2,0,-1):
            print(i*char)
    if height%2 == 1:
        for i in range(1,height//2+2):
            print(i*char)
        for i in range(height//2,0,-1):
            print(i*char)
            

char, height = sys.argv[1], int(sys.argv[2])
print_triangle(char, height)
