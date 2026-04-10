import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import random
from baby_blind_script import new_scrambled_cube, solve_cube

def measure_memo_length(solution_string):
    """
    Returns (edge_length, corner_length, has_parity)
    """
    has_parity = '|' in solution_string
    parts = solution_string.replace('|', '.').split('.')
    edge_length = len(parts[0])
    corner_length = len(parts[1])
    return edge_length, corner_length, has_parity

def run_distribution(num_samples=10000):
    results = []

    for i in range(num_samples):
        if i % 1000 == 0:
            print(f'  {i}/{num_samples}...')
        cube = new_scrambled_cube()
        solution = solve_cube(cube)
        edge_len, corner_len, has_parity = measure_memo_length(solution)
        total = edge_len + corner_len
        results.append((edge_len, corner_len, total, has_parity))

    return results

def summarize(results):
    totals = [r[2] for r in results]
    edge_lens = [r[0] for r in results]
    corner_lens = [r[1] for r in results]
    parity_count = sum(1 for r in results if r[3])

    print(f'\n--- Results over {len(results)} samples ---')
    print(f'\nTotal memo length:')
    print(f'  Min:    {min(totals)}')
    print(f'  Max:    {max(totals)}')
    print(f'  Mean:   {sum(totals)/len(totals):.2f}')

    print(f'\nEdge memo length:')
    print(f'  Min:    {min(edge_lens)}')
    print(f'  Max:    {max(edge_lens)}')
    print(f'  Mean:   {sum(edge_lens)/len(edge_lens):.2f}')

    print(f'\nCorner memo length:')
    print(f'  Min:    {min(corner_lens)}')
    print(f'  Max:    {max(corner_lens)}')
    print(f'  Mean:   {sum(corner_lens)/len(corner_lens):.2f}')

    print(f'\nParity: {parity_count}/{len(results)} ({100*parity_count/len(results):.1f}%)')

    print(f'\nDistribution of total memo length:')
    for length in range(min(totals), max(totals)+1):
        count = totals.count(length)
        bar = '#' * (count * 50 // len(results))
        print(f'  {length:3d}: {bar} ({count})')

if __name__ == '__main__':
    print('Measuring memo distribution...')
    results = run_distribution(num_samples=10000)
    summarize(results)