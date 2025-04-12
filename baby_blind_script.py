import copy
import random
import pickle

import pandas as pd
import kociemba

SOLVED_STATE = {
    'A' : 'A',
    'B' : 'B',
    'C' : 'C',
    'D' : 'D',

    'E' : 'E',
    'F' : 'F',
    'G' : 'G',
    'H' : 'H',

    'I' : 'I',
    'J' : 'J',
    'K' : 'K',
    'L' : 'L',

    'M' : 'M',
    'N' : 'N',
    'O' : 'O',
    'P' : 'P',

    'Q' : 'Q',
    'R' : 'R',
    'S' : 'S',
    'T' : 'T',

    'U' : 'U',
    'V' : 'V',
    'W' : 'W',
    'X' : 'X'
}

SOLVED_CUBE = {
    'edges' : copy.deepcopy(SOLVED_STATE),
    'corners' : copy.deepcopy(SOLVED_STATE)
}

EDGES_DICT = {
    'A' : 'AQ',
    #'B' : 'B',
    'C' : 'CI',
    'D' : 'DE',
    'E' : 'ED',
    'F' : 'FL',
    'G' : 'GX',
    'H' : 'HR',
    'I' : 'IC',
    'J' : 'JP',
    'K' : 'KU',
    'L' : 'LF',
    #'M' : 'M',
    'N' : 'NT',
    'O' : 'OV',
    'P' : 'PJ',
    'Q' : 'QA',
    'R' : 'RH',
    'S' : 'SW',
    'T' : 'TN',
    'U' : 'UK',
    'V' : 'VO',
    'W' : 'WS',
    'X' : 'XG',
}

CORNERS_DICT = { # in clockwise order
    #'A' : 'A',
    'B' : 'BQN',
    'C' : 'CMJ',
    'D' : 'DIF',
    #'E' : 'E',
    'F' : 'FDI',
    'G' : 'GLU',
    'H' : 'HXS',
    'I' : 'IFD',
    'J' : 'JCM',
    'K' : 'KPV',
    'L' : 'LUG',
    'M' : 'MJC',
    'N' : 'NBQ',
    'O' : 'OTW',
    'P' : 'PVK',
    'Q' : 'QNB',
    #'R' : 'R',
    'S' : 'SHX',
    'T' : 'TWO',
    'U' : 'UGL',
    'V' : 'VKP',
    'W' : 'WOT',
    'X' : 'XSH',
}

# operations
def cycle_four_edges(cube, new_cube, to_cycle):
    new_cube['edges'][to_cycle[0]] = cube['edges'][to_cycle[3]]
    new_cube['edges'][to_cycle[1]] = cube['edges'][to_cycle[0]]
    new_cube['edges'][to_cycle[2]] = cube['edges'][to_cycle[1]]
    new_cube['edges'][to_cycle[3]] = cube['edges'][to_cycle[2]]
    
    new_cube['edges'][to_cycle[5]] = cube['edges'][to_cycle[8]]
    new_cube['edges'][to_cycle[6]] = cube['edges'][to_cycle[5]]
    new_cube['edges'][to_cycle[7]] = cube['edges'][to_cycle[6]]
    new_cube['edges'][to_cycle[8]] = cube['edges'][to_cycle[7]]

    return

def cycle_four_corners(cube, new_cube, to_cycle):
    new_cube['corners'][to_cycle[0]] = cube['corners'][to_cycle[3]]
    new_cube['corners'][to_cycle[1]] = cube['corners'][to_cycle[0]]
    new_cube['corners'][to_cycle[2]] = cube['corners'][to_cycle[1]]
    new_cube['corners'][to_cycle[3]] = cube['corners'][to_cycle[2]]
    
    new_cube['corners'][to_cycle[5]] = cube['corners'][to_cycle[8]]
    new_cube['corners'][to_cycle[6]] = cube['corners'][to_cycle[5]]
    new_cube['corners'][to_cycle[7]] = cube['corners'][to_cycle[6]]
    new_cube['corners'][to_cycle[8]] = cube['corners'][to_cycle[7]]

    new_cube['corners'][to_cycle[10]] = cube['corners'][to_cycle[13]]
    new_cube['corners'][to_cycle[11]] = cube['corners'][to_cycle[10]]
    new_cube['corners'][to_cycle[12]] = cube['corners'][to_cycle[11]]
    new_cube['corners'][to_cycle[13]] = cube['corners'][to_cycle[12]]

    return

def R_move(cube):
    new_cube = copy.deepcopy(cube)
    cycle_four_edges(cube, new_cube, 'MNOP BTVJ')
    cycle_four_corners(cube, new_cube, 'MNOP BTVJ CQWK')
    return new_cube

def L_move(cube):
    new_cube = copy.deepcopy(cube)
    cycle_four_edges(cube, new_cube, 'EFGH DLXR')
    cycle_four_corners(cube, new_cube, 'EFGH DLXR AIUS')
    return new_cube

def U_move(cube):
    new_cube = copy.deepcopy(cube)
    cycle_four_edges(cube, new_cube, 'ABCD QMIE')
    cycle_four_corners(cube, new_cube, 'ABCD QMIE RNJF')
    return new_cube

def D_move(cube):
    new_cube = copy.deepcopy(cube)
    cycle_four_edges(cube, new_cube, 'UVWX KOSG')
    cycle_four_corners(cube, new_cube, 'UVWX KOSG LPTH')
    return new_cube

def F_move(cube):
    new_cube = copy.deepcopy(cube)
    cycle_four_edges(cube, new_cube, 'IJKL CPUF')
    cycle_four_corners(cube, new_cube, 'IJKL CPUF DMVG')
    return new_cube

def B_move(cube):
    new_cube = copy.deepcopy(cube)
    cycle_four_edges(cube, new_cube, 'QRST AHWN')
    cycle_four_corners(cube, new_cube, 'QRST AHWN BEXO')
    return new_cube

MOVES = {
    'U' : U_move,
    'D' : D_move,
    'R' : R_move,
    'L' : L_move,
    'F' : F_move,
    'B' : B_move,

    'U2' : lambda x : U_move(U_move(x)),
    'D2' : lambda x : D_move(D_move(x)),
    'R2' : lambda x : R_move(R_move(x)),
    'L2' : lambda x : L_move(L_move(x)),
    'F2' : lambda x : F_move(F_move(x)),
    'B2' : lambda x : B_move(B_move(x)),

    "U'" : lambda x : U_move(U_move(U_move(x))),
    "D'" : lambda x : D_move(D_move(D_move(x))),
    "R'" : lambda x : R_move(R_move(R_move(x))),
    "L'" : lambda x : L_move(L_move(L_move(x))),
    "F'" : lambda x : F_move(F_move(F_move(x))),
    "B'" : lambda x : B_move(B_move(B_move(x))),
}

ALL_MOVES = list(MOVES.keys())

def make_scramble_sequence(scramble_len=50):
    scramble = ''

    most_recent_move = random.choice(ALL_MOVES)
    new_move = random.choice(ALL_MOVES)
    
    for i in range(scramble_len):
        scramble += most_recent_move + ' '
        while new_move[0] == most_recent_move[0]:
            new_move = random.choice(ALL_MOVES)
            
        most_recent_move = new_move

    return scramble

def swap_two_edges(cube, edge_1, edge_2):
    '''
    For example: swap_two_edges(messy_cube, 'AQ', 'BM')
    '''
    # swaps the piece specified by edge_1 with the piece specified by edge_2.
    # Specifically, we are swapping
    # cube['edges'][edge_1[0]] with cube['edges'][edge_2[0]], and
    # cube['edges'][edge_1[1]] with cube['edges'][edge_2[1]]

    temp_0 = cube['edges'][edge_1[0]]
    temp_1 = cube['edges'][edge_1[1]]

    cube['edges'][edge_1[0]] = cube['edges'][edge_2[0]]
    cube['edges'][edge_1[1]] = cube['edges'][edge_2[1]]

    cube['edges'][edge_2[0]] = temp_0
    cube['edges'][edge_2[1]] = temp_1

    # in theory, we could maybe do
    # temp = cube['edges'][edge_1]
    # cube['edges'][edge_1] = cube['edges'][edge_2]
    # cube['edges'][edge_2] = temp
    # but that is hard to read/understand. The operation of
    # "set the (dict) values associated with this list of keys
    # to this list of values" is not very intuitive


def swap_two_corners(cube, corner_1, corner_2):
    '''
    For example: swap_two_corners(messy_cube, 'DIF', 'CMJ')
    Ordering can be clockwise or counterclockwise, as long as
    it is the same between the two corners.
    '''

    temp_0 = cube['corners'][corner_1[0]]
    temp_1 = cube['corners'][corner_1[1]]
    temp_2 = cube['corners'][corner_1[2]]

    cube['corners'][corner_1[0]] = cube['corners'][corner_2[0]]
    cube['corners'][corner_1[1]] = cube['corners'][corner_2[1]]
    cube['corners'][corner_1[2]] = cube['corners'][corner_2[2]]

    cube['corners'][corner_2[0]] = temp_0
    cube['corners'][corner_2[1]] = temp_1
    cube['corners'][corner_2[2]] = temp_2


def fix_edge_in_buffer(cube):
    buffer = cube['edges']['B']
    piece_in_buffer = EDGES_DICT[buffer]

    new_cube = swap_two_edges(cube, 'BM', piece_in_buffer)


def fix_corner_in_buffer(cube):
    buffer = cube['corners']['E']
    piece_in_buffer = CORNERS_DICT[buffer]

    new_cube = swap_two_corners(cube, 'ERA', piece_in_buffer)
    
def find_unsolved_edge_slot(cube, priority=None):
    pieces_to_search_in_order = ''.join(list(SOLVED_STATE.keys()))
    
    if priority:
        pieces_to_search_in_order = priority + pieces_to_search_in_order
    
    for one_edge in pieces_to_search_in_order:
        if one_edge != cube['edges'][one_edge] and one_edge not in 'BM':
            # if piece is unsolved and not in buffer slot
            return one_edge
    
    print('This should never be reached! All edges are solved')
    
    
def find_unsolved_corner_slot(cube, priority=None):
    pieces_to_search_in_order = ''.join(list(SOLVED_STATE.keys()))
    
    if priority:
        pieces_to_search_in_order = priority + pieces_to_search_in_order
    
    for one_corner in pieces_to_search_in_order:
        if one_corner != cube['corners'][one_corner] and one_corner not in 'AER':
            # if piece is unsolved and not in buffer slot
            return one_corner
    
    print('This should never be reached! All corners are solved')
    
    
def solve_cube(scrambled_cube, verbose=False, priority=None):
    new_cube = copy.deepcopy(scrambled_cube)
    solve_string = ''
    # solve edges
    while new_cube['edges'] != SOLVED_STATE:
        buffer = new_cube['edges']['B']
        if buffer not in 'BM':
            # let's say buffer == 'A'
            #swap(new_cube, 'BM', 'AQ')

            # if the buffer is NOT the white/red piece, then the buffer is
            # holding a piece that belongs somewhere else. Let's put it where
            # it belongs
            fix_edge_in_buffer(new_cube)
            swap_two_corners(new_cube, 'CMJ', 'BQN')
            solve_string += buffer
        else:
            # if buffer == 'B' or buffer == 'M' start new cycle
            # specifically, find an unsolved edge and swap with it
            unsolved_edge_slot = find_unsolved_edge_slot(new_cube, priority)
            unsolved_edge_piece = EDGES_DICT[unsolved_edge_slot]
            swap_two_edges(new_cube, 'BM', unsolved_edge_piece)
            swap_two_corners(new_cube, 'CMJ', 'BQN')
            if verbose:
                solve_string += '/'
            solve_string += unsolved_edge_slot

    edge_count = len(solve_string.replace('/', ''))
    if edge_count % 2 == 1:
        # parity
        solve_string += '|'
        
        # Ra perm
        swap_two_edges(new_cube, 'AQ', 'DE')
        swap_two_corners(new_cube, 'CMJ', 'BQN')
    else:
        # no parity
        solve_string += '.'
        
    # solve corners
    while new_cube['corners'] != SOLVED_STATE:
        buffer = new_cube['corners']['E']
        if buffer not in 'AER':
            fix_corner_in_buffer(new_cube)
            swap_two_edges(new_cube, 'AQ', 'DE')
            solve_string += buffer
        else:
            # new cycle
            unsolved_corner_slot = find_unsolved_corner_slot(new_cube, priority)
            unsolved_corner_piece = CORNERS_DICT[unsolved_corner_slot]
            swap_two_corners(new_cube, 'ERA', unsolved_corner_piece)
            swap_two_edges(new_cube, 'AQ', 'DE')
            if verbose:
                solve_string += '/'
            solve_string += unsolved_corner_slot
            
    return solve_string



def execute_algorithm(cube, algorithm_string):
    new_cube = copy.deepcopy(cube)

    algorithm_list = algorithm_string.split()
    #print(algorithm_list)
    for move in algorithm_list:
        method_for_move = MOVES[move]
        new_cube = method_for_move(new_cube)

    return new_cube


def new_scrambled_cube(scramble_len=25):
    scramble_sequence = make_scramble_sequence(scramble_len=scramble_len)
    scrambled_cube = execute_algorithm(SOLVED_CUBE, scramble_sequence)
    return scrambled_cube


# we can probably delete some of these functions... like this one
def run_simulation(num_sims=1000, scramble_len=25):
    matrix = []

    print(f'Starting simulation... with num_sims={num_sims}')
    for i in range(num_sims):
        scramble = make_scramble_sequence(scramble_len=scramble_len)
        messy_cube = execute_algorithm(SOLVED_CUBE, scramble)
        sol = solve_cube(messy_cube)
        sol_length = len(sol) - 1

        matrix.append([sol_length, scramble, sol])

    print('Ending simulation!')
    return pd.DataFrame(matrix, columns=['Length', 'Scramble', 'Solution'])




def scramble_cube_with_solution_string(solution_string):
    new_cube = copy.deepcopy(SOLVED_CUBE)
    edge_solution, corner_solution = solution_string.replace('|', '.').split('.')
    
    for i in range(len(edge_solution)):
        one_edge = edge_solution[len(edge_solution) - i - 1]
        unsolved_edge_piece = EDGES_DICT[one_edge]
        swap_two_edges(new_cube, 'BM', unsolved_edge_piece)

    for i in range(len(corner_solution)):
        one_corner = corner_solution[len(corner_solution) - i - 1]
        unsolved_corner_piece = CORNERS_DICT[one_corner]
        swap_two_corners(new_cube, 'ERA', unsolved_corner_piece)
        
    return new_cube


def simplify_solution(solution_string, priority=None):
    new_cube = scramble_cube_with_solution_string(solution_string)
    simple_solution = solve_cube(new_cube, verbose=False, priority=priority)
    return simple_solution


# make sure nonsense_len is even to avoid parity
def generate_nonsense_solution(pool, nonsense_len=30):
    nonsense_string = ''
    for _ in range(nonsense_len):
        nonsense_string += random.choice(pool)
        
    return nonsense_string