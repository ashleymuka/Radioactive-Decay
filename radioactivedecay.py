'''
Author: Ashley Muka
Assignment Title: Radioactive decay
Assignment Description:complete function to implement formulas
Due Date:09/29/2023
Date Created:09/27/2023
Date Last Modified:09/28/2023

'''

#data abstraction
import math

#process
def compute_Nt(NO, t, T):
    
    Nt = NO * math.e ** (-0.693 * t / T)
    return Nt


def compute_T(NO, Nt, t):
    
    T = -0.693 * t / math.log(Nt / NO)
    return T


if __name__ == "__main__":

#input
    
    choice = input()
    NO = float(input())
    t = float(input())
    T = float(input())

#process and output    
    if choice == "N":
        
        Nt = compute_Nt(NO, t, T)

        print(f'Nt = {Nt:.4f}')


    elif choice == "T":

        T = compute_T(NO, Nt, t)

        print(f'T = {T:.4f}')

        



