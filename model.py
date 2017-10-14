import numpy as np



class Model:

    boards = {'1-1': 'board-1-1.txt',
              '1-2': 'board-1-2.txt',
              '1-3': 'board-1-3-.txt',
              '1-4': 'board-1-4.txt',
              '2-1': 'board-2-1.txt',
              '2-2': 'board-2-2.txt',
              '2-3': 'board-2-3-.txt',
              '2-4': 'board-2-4.txt'}

    def __init__(self, board):
        b, s, e = self.read_board(Model.boards[board])
        self.board = b
        self.start_pos = s
        self.end_pos = e

    def h(self, state):
        return (state[0]-self.end_pos[0])**2 + (state[1]-self.end_pos[1])**2

    def expand_state(self, state):
        ret = []
        if state[0] != 0 and self.board[state[1]][state[0]] != '#'

    @staticmethod
    def read_board(file_path):
        ret = []
        start = (0, 0)
        end = (0, 0)
        with open('boards/' + file_path, 'r') as f:
            for y, line in enumerate(f):
                row = []
                for x, tile in enumerate(line):
                    row.append(tile)
                    if tile == 'A':
                        start = (x, y)
                    elif tile == 'B':
                        end = (x, y)
        return ret, start, end