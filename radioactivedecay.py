'''
Description: complete function to implement formula for radioactive decay
'''

import math

def compute_Nt(NO, t, T):
    
    Nt = NO * math.e ** (-0.693 * t / T)
    return Nt


def compute_T(NO, Nt, t):
    
    T = -0.693 * t / math.log(Nt / NO)
    return T


if __name__ == "__main__":
    
    choice = input()
    NO = float(input())
    t = float(input())
    T = float(input())


    if choice == "N":
        
        Nt = compute_Nt(NO, t, T)
        print(f'Nt = {Nt:.4f}')


    elif choice == "T":

        T = compute_T(NO, Nt, t)
        print(f'T = {T:.4f}')

        



