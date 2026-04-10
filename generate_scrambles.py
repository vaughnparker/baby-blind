from baby_blind_script import generate_baby_scrambles

# Edge pools
EDGES_LEVEL_1 = "ACD"
EDGES_LEVEL_2 = "ACDUVWX"
EDGES_LEVEL_3 = "ACDUVWXLRJT"
EDGES_LEVEL_4 = "ACDUVWXLRJTFHNP"
EDGES_LEVEL_5 = "ACDUVWXLRJTFHNPEIQ"
EDGES_LEVEL_6 = "ACDUVWXLRJTFHNPEIQKSGO"

# Corner pools
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

if __name__ == '__main__':
    print('Generating edges scrambles...')
    for i, pool in enumerate(EDGES_POOLS):
        print(f'  Edges level {i+1}...')
        scrambles = generate_baby_scrambles(pool, count=500, mode='edges')
        with open(f'edges_level_{i+1}_scrambles.txt', 'w') as f:
            f.write(scrambles)

    print('Generating corners scrambles...')
    for i, pool in enumerate(CORNERS_POOLS):
        print(f'  Corners level {i+1}...')
        scrambles = generate_baby_scrambles(pool, count=500, mode='corners')
        with open(f'corners_level_{i+1}_scrambles.txt', 'w') as f:
            f.write(scrambles)

    print('Done!')