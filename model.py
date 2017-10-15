import tkinter as tk
import time

class Model:
    # A Dictionary of different boards
    boards = {
        '1-1': 'board-1-1.txt',
        '1-2': 'board-1-2.txt',
        '1-3': 'board-1-3.txt',
        '1-4': 'board-1-4.txt',
        '2-1': 'board-2-1.txt',
        '2-2': 'board-2-2.txt',
        '2-3': 'board-2-3.txt',
        '2-4': 'board-2-4.txt'
    }
    # Dictionary for tile penalties
    penalties = {
        'w': 100,
        'm': 50,
        'f': 10,
        'g': 5,
        'r': 1,
        '.': 1,
        'B': 1,
        'A': 1
    }
    # Dictionary for tile colors
    colors = {
        'A': 'lime',
        'B': 'red',
        '#': 'black',
        '.': 'white',
        'm': 'gray',
        'w': 'blue',
        'r': 'burlywood4',
        'f': 'forest green',
        'g': 'yellow green'
    }

    def __init__(self, board, window_name='title'):
        b, s, e = self.read_board(Model.boards[board])
        self.board = b
        self.start_pos = s
        self.end_pos = e
        self.y_len = len(b)
        self.x_len = len(b[0])

        self.tk = None
        self.canvas = None
        self.tile_size = None
        self.window_name = window_name

    def h(self, state):
        # City block distance
        return abs(state[0]-self.end_pos[0]) + abs(state[1]-self.end_pos[1])
        #np.sqrt((state[0]-self.end_pos[0])**2 + (state[1]-self.end_pos[1])**2)

    def g(self, state):
        # returns tile traversal cost
        return Model.penalties[self.board[state[1]][state[0]]]

    def expand_state(self, state):
        x = state[0]
        y = state[1]
        ret = []
        if x != 0 and self.board[y][x-1] != '#':
            ret.append((x-1, y))
        if x != self.x_len-1 and self.board[y][x+1] != '#':
            ret.append((x+1, y))
        if y != 0 and self.board[y-1][x] != '#':
            ret.append((x, y-1))
        if y != self.y_len-1 and self.board[y+1][x] != '#':
            ret.append((x, y+1))
        return ret

    def is_solution(self, state):
        # Self explanatory
        return state == self.end_pos

    def _draw_board(self):
        width = 800
        height = 800

        y_ratio = self.y_len/self.x_len
        x_ratio = self.x_len/self.y_len

        # scale board within 800x800
        if y_ratio < x_ratio:
            x_ratio = y_ratio
            y_ratio = 1
            tile_size = width/self.x_len
        else:
            y_ratio = x_ratio
            x_ratio = 1
            tile_size = height/self.y_len

        self.tile_size = tile_size

        if self.tk is None:
            self.tk = tk.Tk(className=self.window_name)
            self.canvas = tk.Canvas(self.tk, height=height*x_ratio, width=width*y_ratio)
            self.canvas.pack()
        # Draw tiles
        for y, line in enumerate(self.board):
            for x, p in enumerate(line):
                self.canvas.create_rectangle(x*tile_size, y*tile_size, (x+1)*tile_size, (y+1)*tile_size,
                                             fill=Model.colors[p])

    def visualize_progress(self, expanded_nodes, frontier_nodes):
        if self.tile_size is None:
            self._draw_board()
        tile_size = self.tile_size
        self.canvas.delete('progress')
        # Draw nodes in frontier
        for f in frontier_nodes:
            x = f[0]
            y = f[1]
            star = [0, 30, 30, 30, 40, 0, 50, 30, 80, 30, 55, 50, 65, 80, 40, 60, 15, 80, 25, 50]
            star = [(v*(tile_size/100) + (x if i % 2 == 0 else y)*tile_size) + tile_size/10 for i, v in enumerate(star)]
            self.canvas.create_polygon(star, fill='goldenrod', tag='progress')

        # Draw expanded nodes
        for e in expanded_nodes:
            x = e[0]
            y = e[1]
            cross = [1, 0, 6, 5, 11, 0, 12, 1, 7, 6, 12, 11, 11, 12, 6, 7, 1, 12, 0, 11, 5, 6, 0, 1]
            cross = [(v*(tile_size/20) + ((x if i%2==0 else y) * tile_size)) + tile_size/5 for (i, v) in enumerate(cross)]
            self.canvas.create_polygon(cross, tag='progress')
        self.tk.update()
        time.sleep(0.1)

    def visualize_solution(self, solution_path, expanded_nodes=None, frontier_nodes=None):
        if self.tile_size is None:

            self._draw_board()
        self.canvas.delete('progress')
        tile_size = self.tile_size
        # Draw nodes in frontier
        if frontier_nodes is not None:
            for f in frontier_nodes:
                x = f[0]
                y = f[1]
                star = [0, 30, 30, 30, 40, 0, 50, 30, 80, 30, 55, 50, 65, 80, 40, 60, 15, 80, 25, 50]
                star = [(v*(tile_size/100) + (x if i % 2 == 0 else y)*tile_size) + tile_size/10 for i, v in enumerate(star)]
                self.canvas.create_polygon(star, fill='goldenrod')
        # Draw expanded nodes
        if expanded_nodes is not None:
            for e in expanded_nodes:
                x = e[0]
                y = e[1]
                cross = [1, 0, 6, 5, 11, 0, 12, 1, 7, 6, 12, 11, 11, 12, 6, 7, 1, 12, 0, 11, 5, 6, 0, 1]
                cross = [(v*(tile_size/20) + ((x if i%2==0 else y) * tile_size)) + tile_size/5 for (i, v) in enumerate(cross)]
                self.canvas.create_polygon(cross)
        # Draw solution path
        for n in solution_path:
            s = tile_size/2.5
            self.canvas.create_oval(n[0]*tile_size+s, n[1]*tile_size+s,
                                    (n[0]+1)*tile_size-s, (n[1]+1)*tile_size-s, fill='black')
            time.sleep(0.1)
            self.tk.update()

        self.tk.destroy()

    @staticmethod
    def read_board(file_path):
        ret = []
        start = (0, 0)
        end = (0, 0)
        with open('boards/' + file_path, 'r') as f:
            for y, line in enumerate(f):
                row = []
                for x, tile in enumerate(line):
                    if tile != '\n':
                        row.append(tile)
                    if tile == 'A':
                        start = (x, y)
                    elif tile == 'B':
                        end = (x, y)
                ret.append(row)
        return ret, start, end
