import random

white_pieces = 9
black_pieces = 9

possible_positions = [
    11, 12, 13, 14, 15, 16, 17, 18,
    21, 22, 23, 24, 25, 26, 27, 28,
    31, 32, 33, 34, 35, 36, 37, 38
    ]

mill_positions = [
    (11, 12, 13), (13, 14, 15), (15, 16, 17), (17, 18, 11),
    (21, 22, 23), (23, 24, 25), (25, 26, 27), (27, 28, 21),
    (31, 32, 33), (33, 34, 35), (35, 36, 37), (37, 38, 31),
    (12, 22, 32), (14, 24, 34), (16, 26, 36), (18, 28, 38)
    ]

occupied_positions = []

def turn():
    next_turn_pos = random.randint(0, len(possible_positions))
    possible_positions.pop(next_turn_pos)

def MCTS():
    pass 

if __name__ == "__main__":
    while True:
        print("Available positions: ", possible_positions)
        user_turn_pos = int(input("Enter Position where you want to place a piece on: "))
        if user_turn_pos in possible_positions:
            pass
        else:
            print("The position you selected was not available. Try again: ")
        turn()
        MCTS()
    