import copy
import random
import pickle

import pandas as pd
import kociemba

SIDE_DICT = {
    'A': 'U',
    'B': 'U',
    'C': 'U',
    'D': 'U',
    'E': 'L',
    'F': 'L',
    'G': 'L',
    'H': 'L',
    'I': 'F',
    'J': 'F',
    'K': 'F',
    'L': 'F',
    'M': 'R',
    'N': 'R',
    'O': 'R',
    'P': 'R',
    'Q': 'B',
    'R': 'B',
    'S': 'B',
    'T': 'B',
    'U': 'D',
    'V': 'D',
    'W': 'D',
    'X': 'D'
}

def get_kociemba_string(cube):
    k_string = ''
    
    # U side
    k_string += SIDE_DICT[cube['corners']['A']]
    k_string += SIDE_DICT[cube['edges']['A']]
    k_string += SIDE_DICT[cube['corners']['B']]
    k_string += SIDE_DICT[cube['edges']['D']]
    k_string += 'U'
    k_string += SIDE_DICT[cube['edges']['B']]
    k_string += SIDE_DICT[cube['corners']['D']]
    k_string += SIDE_DICT[cube['edges']['C']]
    k_string += SIDE_DICT[cube['corners']['C']]
    
    # R side
    k_string += SIDE_DICT[cube['corners']['M']]
    k_string += SIDE_DICT[cube['edges']['M']]
    k_string += SIDE_DICT[cube['corners']['N']]
    k_string += SIDE_DICT[cube['edges']['P']]
    k_string += 'R'
    k_string += SIDE_DICT[cube['edges']['N']]
    k_string += SIDE_DICT[cube['corners']['P']]
    k_string += SIDE_DICT[cube['edges']['O']]
    k_string += SIDE_DICT[cube['corners']['O']]
    
    # F side
    k_string += SIDE_DICT[cube['corners']['I']]
    k_string += SIDE_DICT[cube['edges']['I']]
    k_string += SIDE_DICT[cube['corners']['J']]
    k_string += SIDE_DICT[cube['edges']['L']]
    k_string += 'F'
    k_string += SIDE_DICT[cube['edges']['J']]
    k_string += SIDE_DICT[cube['corners']['L']]
    k_string += SIDE_DICT[cube['edges']['K']]
    k_string += SIDE_DICT[cube['corners']['K']]
    
    # D side
    k_string += SIDE_DICT[cube['corners']['U']]
    k_string += SIDE_DICT[cube['edges']['U']]
    k_string += SIDE_DICT[cube['corners']['V']]
    k_string += SIDE_DICT[cube['edges']['X']]
    k_string += 'D'
    k_string += SIDE_DICT[cube['edges']['V']]
    k_string += SIDE_DICT[cube['corners']['X']]
    k_string += SIDE_DICT[cube['edges']['W']]
    k_string += SIDE_DICT[cube['corners']['W']]
    
    # L side
    k_string += SIDE_DICT[cube['corners']['E']]
    k_string += SIDE_DICT[cube['edges']['E']]
    k_string += SIDE_DICT[cube['corners']['F']]
    k_string += SIDE_DICT[cube['edges']['H']]
    k_string += 'L'
    k_string += SIDE_DICT[cube['edges']['F']]
    k_string += SIDE_DICT[cube['corners']['H']]
    k_string += SIDE_DICT[cube['edges']['G']]
    k_string += SIDE_DICT[cube['corners']['G']]
    
    # B side
    k_string += SIDE_DICT[cube['corners']['Q']]
    k_string += SIDE_DICT[cube['edges']['Q']]
    k_string += SIDE_DICT[cube['corners']['R']]
    k_string += SIDE_DICT[cube['edges']['T']]
    k_string += 'B'
    k_string += SIDE_DICT[cube['edges']['R']]
    k_string += SIDE_DICT[cube['corners']['T']]
    k_string += SIDE_DICT[cube['edges']['S']]
    k_string += SIDE_DICT[cube['corners']['S']]
    
    return k_string



def get_solve_sequence(scrambled_cube, reverse=False):
    one_k_string = get_kociemba_string(scrambled_cube)
    solve_string = kociemba.solve(one_k_string)
    
    if reverse:
        reversed_string = ''
        for move in solve_string.split():
            if len(move) == 1: # clockwise 90 degrees becomes counterclockwise 90 degrees
                reversed_string = move + '\' ' + reversed_string
            elif move[1] == '2': # 180 degree turns stay the same
                reversed_string = move + ' ' + reversed_string
            else: # counterclockwise 90 degree turns become clockwise 90 degree turns
                reversed_string = move[0] + ' ' + reversed_string
        return reversed_string.strip()
    else:
        return solve_string 