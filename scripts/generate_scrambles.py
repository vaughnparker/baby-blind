import sys
import os
import random
sys.path.insert(0, os.path.dirname(__file__))

from baby_blind_script import (
    generate_nonsense_solution,
    simplify_solution,
    scramble_cube_with_solution_string,
    new_scrambled_cube,
    solve_cube,
    EDGES_DICT,
    CORNERS_DICT
)
from kociemba_script import get_solve_sequence

# ── Constants ────────────────────────────────────────────────────────────────
SCRAMBLES_PER_LEVEL = 500
MAX_ATTEMPTS = 50000  # increase this if a level is hard to fill

# ── Phase 1 pools ─────────────────────────────────────────────────────────────
EDGES_LEVEL_1 = "ACD"
EDGES_LEVEL_2 = "ACDUVWX"
EDGES_LEVEL_3 = "ACDUVWXLRJT"
EDGES_LEVEL_4 = "ACDUVWXLRJTFHNP"
EDGES_LEVEL_5 = "ACDUVWXLRJTFHNPEIQ"
EDGES_LEVEL_6 = "ACDUVWXLRJTFHNPEIQKSGO"

CORNERS_LEVEL_1 = "UVWX"
CORNERS_LEVEL_2 = "UVWXBCD"
CORNERS_LEVEL_3 = "UVWXBCDIJQ"
CORNERS_LEVEL_4 = "UVWXBCDIJQFMN"
CORNERS_LEVEL_5 = "UVWXBCDIJQFMNKLST"
CORNERS_LEVEL_6 = "UVWXBCDIJQFMNKLSTGHOP"

EDGES_POOLS = [
    EDGES_LEVEL_1, EDGES_LEVEL_2, EDGES_LEVEL_3,
    EDGES_LEVEL_4, EDGES_LEVEL_5, EDGES_LEVEL_6
]

CORNERS_POOLS = [
    CORNERS_LEVEL_1, CORNERS_LEVEL_2, CORNERS_LEVEL_3,
    CORNERS_LEVEL_4, CORNERS_LEVEL_5, CORNERS_LEVEL_6
]

FULL_EDGES_POOL = EDGES_LEVEL_6
FULL_CORNERS_POOL = CORNERS_LEVEL_6

# ── Phase 1 generation ────────────────────────────────────────────────────────
def generate_baby_scrambles(letter_pool, count=500, mode='edges'):
    """
    mode: 'edges' for edges-only, 'corners' for corners-only
    """
    to_return = ""

    for i in range(count):
        one_nons = generate_nonsense_solution(letter_pool)

        if mode == 'edges':
            solution_string = simplify_solution(one_nons + '.', priority=letter_pool)
        else:  # corners
            solution_string = '.' + simplify_solution('.' + one_nons, priority=letter_pool).split('.')[1]

        one_cube = scramble_cube_with_solution_string(solution_string)
        k_solution = get_solve_sequence(one_cube, reverse=True)
        to_return += "\n" + k_solution

    return to_return


# ── Memo length helpers ───────────────────────────────────────────────────────
def parse_solution(solution_string):
    has_parity = '|' in solution_string
    parts = solution_string.replace('|', '.').split('.')
    edge_len = len(parts[0])
    corner_len = len(parts[1])
    total = edge_len + corner_len
    return edge_len, corner_len, total, has_parity


# ── Phase 2A - constructed short memos ───────────────────────────────────────
def generate_phase_2a_scramble(target_length, allow_parity=False):
    """
    Constructs a scramble with exactly target_length total letters, no parity
    unless allow_parity is True.
    """
    for _ in range(MAX_ATTEMPTS):
        # randomly split target_length between edges and corners
        # edge count must be even for no parity
        if allow_parity:
            edge_count = random.randint(0, target_length)
        else:
            edge_count = random.choice(
                [n for n in range(0, target_length + 1, 2) 
                 if 0 <= target_length - n <= len(FULL_CORNERS_POOL)]
            )
        corner_count = target_length - edge_count

        if edge_count > len(FULL_EDGES_POOL) or corner_count > len(FULL_CORNERS_POOL):
            continue

        # build solution string
        edge_memo = ''.join(random.choices(FULL_EDGES_POOL, k=edge_count))
        corner_memo = ''.join(random.choices(FULL_CORNERS_POOL, k=corner_count))
        raw_solution = edge_memo + '.' + corner_memo

        simplified = simplify_solution(raw_solution, priority=FULL_EDGES_POOL)
        e_len, c_len, total, has_parity = parse_solution(simplified)

        if total != target_length:
            continue
        if not allow_parity and has_parity:
            continue
        if allow_parity and not has_parity:
            continue

        cube = scramble_cube_with_solution_string(simplified)
        return get_solve_sequence(cube, reverse=True)

    return None


def generate_phase_2a(target_length, count=SCRAMBLES_PER_LEVEL, allow_parity=False):
    results = []
    attempts = 0
    while len(results) < count and attempts < MAX_ATTEMPTS:
        attempts += 1
        scramble = generate_phase_2a_scramble(target_length, allow_parity=allow_parity)
        if scramble:
            results.append(scramble)
    print(f'    Got {len(results)}/{count} after {attempts} attempts')
    return '\n'.join(results)


# ── Phase 2B - natural memos, no parity ──────────────────────────────────────
def generate_phase_2b(target_lengths, count=SCRAMBLES_PER_LEVEL):
    """
    target_lengths: a list of acceptable total memo lengths, e.g. [16] or [14,16,18,20,22,24,26]
    No parity.
    """
    results = []
    attempts = 0
    while len(results) < count and attempts < MAX_ATTEMPTS:
        attempts += 1
        cube = new_scrambled_cube()
        solution = solve_cube(cube)
        e_len, c_len, total, has_parity = parse_solution(solution)
        if total in target_lengths and not has_parity:
            scramble = get_solve_sequence(cube, reverse=True)
            results.append(scramble)
    print(f'    Got {len(results)}/{count} after {attempts} attempts')
    return '\n'.join(results)


# ── Phase 2C - parity guaranteed ─────────────────────────────────────────────
def generate_phase_2c(target_lengths, count=SCRAMBLES_PER_LEVEL):
    """
    target_lengths: a list of acceptable total memo lengths
    Parity guaranteed.
    """
    results = []
    attempts = 0
    while len(results) < count and attempts < MAX_ATTEMPTS:
        attempts += 1
        cube = new_scrambled_cube()
        solution = solve_cube(cube)
        e_len, c_len, total, has_parity = parse_solution(solution)
        if total in target_lengths and has_parity:
            scramble = get_solve_sequence(cube, reverse=True)
            results.append(scramble)
    print(f'    Got {len(results)}/{count} after {attempts} attempts')
    return '\n'.join(results)


# ── Phase 2D - full difficulty ────────────────────────────────────────────────
def generate_phase_2d(count=SCRAMBLES_PER_LEVEL):
    """
    No restrictions - full random scrambles.
    """
    results = []
    for _ in range(count):
        cube = new_scrambled_cube()
        scramble = get_solve_sequence(cube, reverse=True)
        results.append(scramble)
    return '\n'.join(results)


# ── File writing helper ───────────────────────────────────────────────────────
def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f'    Written: {path}')


# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    base = os.path.dirname(os.path.dirname(__file__))

    # Phase 1
    print('Generating Phase 1 edge scrambles...')
    for i, pool in enumerate(EDGES_POOLS):
        print(f'  Edges level {i+1}...')
        scrambles = generate_baby_scrambles(pool, count=SCRAMBLES_PER_LEVEL, mode='edges')
        write_file(f'{base}/phase_1_recog/edges/edges_level_{i+1}_scrambles.txt', scrambles)

    print('Generating Phase 1 corner scrambles...')
    for i, pool in enumerate(CORNERS_POOLS):
        print(f'  Corners level {i+1}...')
        scrambles = generate_baby_scrambles(pool, count=SCRAMBLES_PER_LEVEL, mode='corners')
        write_file(f'{base}/phase_1_recog/corners/corners_level_{i+1}_scrambles.txt', scrambles)

    # Phase 2A
    print('Generating Phase 2A scrambles (constructed, no parity)...')
    for length in [2, 4, 6, 8, 10, 12]:
        print(f'  Length {length}...')
        scrambles = generate_phase_2a(length)
        write_file(f'{base}/phase_2_memo/phase_2a_constructed/memo_length_{length}_scrambles.txt', scrambles)

    # Phase 2B
    print('Generating Phase 2B scrambles (natural, no parity)...')
    for length in [16, 18, 20, 22]:
        print(f'  Length {length}...')
        scrambles = generate_phase_2b([length])
        write_file(f'{base}/phase_2_memo/phase_2b_no_parity/memo_length_{length}_scrambles.txt', scrambles)

    # Phase 2C
    print('Generating Phase 2C scrambles (parity guaranteed)...')
    print('  Length 2 (constructed)...')
    scrambles = generate_phase_2a(2, allow_parity=True)
    write_file(f'{base}/phase_2_memo/phase_2c_parity_guaranteed/memo_length_2_scrambles.txt', scrambles)

    print('  Length 16 (natural)...')
    scrambles = generate_phase_2c([16])
    write_file(f'{base}/phase_2_memo/phase_2c_parity_guaranteed/memo_length_16_scrambles.txt', scrambles)

    # Phase 2D
    print('Generating Phase 2D scrambles (full difficulty)...')
    scrambles = generate_phase_2d()
    write_file(f'{base}/phase_2_memo/phase_2d_full/full_scrambles.txt', scrambles)

    print('All done!')