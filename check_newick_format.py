#!/usr/bin/env python3
import sys 

def formatcheck(char: str) -> None:
    """
    Check whether all the parenthesis are paired
    
    Parameter:
    - char (str): The input parenthesis
    """
    
   
    if char.count("(") == char.count(")") and list(char)[0] == "(" and list(char)[-1] == ")":
        print("PAIRED")
    else:
        print("NOT PAIRED")
    

char = sys.argv[1]
formatcheck(char)