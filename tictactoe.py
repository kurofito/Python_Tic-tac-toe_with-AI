from random import choice as choose


class Tictac:
    def __init__(self):
        self.coordinates = {'1 3': 0, '2 3': 1, '3 3': 2, '1 2': 3, '2 2': 4, '3 2': 5, '1 1': 6, '2 1': 7, '3 1': 8}
        self.game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.board_index = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.breaker = 0
        self.start = True
        self.input = None
        self.comp_sign = None
        self.enemy_sign = None
        self.result = None
        self.state = None
        self.comm = {'start easy easy': {2: self.easy_x, 3: self.easy_o},
                     'start easy user': {2: self.easy_x, 3: self.human_x},
                     'start user easy': {2: self.human_x, 3: self.easy_x},
                     'start user user': {2: self.human_o, 3: self.human_x}}

    def display(self):
        print(f'---------\n'
              f'| {self.game_board[0]} {self.game_board[1]} {self.game_board[2]} |\n'
              f'| {self.game_board[3]} {self.game_board[4]} {self.game_board[5]} |\n'
              f'| {self.game_board[6]} {self.game_board[7]} {self.game_board[8]} |\n'
              f'---------')

    def psigns(self):
        pd = {'start easy user': {'ai': 'X', 'user': 'O'}, 'start user easy': {'user': 'X', 'ai': 'O'},
              'start easy easy': {'ai': 'X', 'user': 'O'}, 'start user user': {'ai': 'X', 'user': 'O'},
              'start medium user': {'ai': 'X', 'user': 'O'}, 'start user medium': {'user': 'X', 'ai': 'O'},
              'start medium medium': {'ai': 'X', 'user': 'O'}, 'start medium easy': {'ai': 'X', 'user': 'O'},
              'start easy medium': {'ai': 'O', 'user': 'X'},
              'start hard user': {'ai': 'X', 'user': 'O'}, 'start user hard': {'ai': 'O', 'user': 'X'},
              'start hard hard': {'ai': 'X', 'user': 'O'}, 'start hard easy': {'ai': 'X', 'user': 'O'},
              'start easy hard': {'ai': 'O', 'user': 'X'}, 'start hard medium': {'ai': 'X', 'user': 'O'},
              'start medium hard': {'ai': 'O', 'user': 'X'},
              'exit': {'ai': 'X', 'user': 'O'}}
        comp_s, self.comp_sign = pd[self.input]['ai'], pd[self.input]['ai']
        enemy_s, self.enemy_sign = pd[self.input]['user'], pd[self.input]['user']
        return comp_s, enemy_s

    def checker(self, sign):
        while True:
            try:
                datum = input('Enter the coordinates: ')
                value_check = int(datum.replace(' ', ''))  
                key_check = self.game_board[self.coordinates[datum]]
                num = self.coordinates[datum]
                if key_check == 'X' or key_check == 'O':
                    print('This cell is occupied! Choose another one!')
                else:
                    self.game_board[num] = sign
                    self.board_index.remove(num)
                    break
            except ValueError:
                print('You should enter numbers!')
            except KeyError:
                print('Coordinates should be from 1 to 3!')

    def reset(self):
        self.game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.board_index = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def wincheck(self):
        matrix = [self.game_board[:3], self.game_board[3:6], self.game_board[6:]]
        vmatrix = [[matrix[j][i] for j in range(3)] for i in range(3)]
        diagonal = [[matrix[0][0], matrix[1][1], matrix[2][2]], [matrix[0][2], matrix[1][1], matrix[2][0]]]
        return matrix + vmatrix + diagonal

    def parser(self):
        self.state = self.wincheck()
        self.result = ['null' if ' ' not in x else x for x in self.state]
        checker = [x for dat in self.state for x in dat]
        rd = [''.join(x) for x in self.state]
        return rd, checker

    def winner(self):
        parser = self.parser()
        if 'XXX' in parser[0]:
            print('X wins\n')
            self.reset()
            self.breaker += 1
        elif 'OOO' in parser[0]:
            print('O wins\n')
            self.reset()
            self.breaker += 1
        elif ' ' not in parser[1]:
            print('Draw\n')
            self.reset()
            self.breaker += 1

    def human_move(self, sign, index):
        self.checker(sign[index])
        self.display()
        self.winner()

    def human_x(self):
        self.human_move(self.psigns(), 1)

    def human_o(self):
        self.human_move(self.psigns(), 0)

    def printing(self):
        print('Making move level "easy"')

    def ai(self, x):
        ai = choose(self.board_index)
        self.game_board[ai] = x
        self.board_index.remove(ai)
        self.display()
        self.winner()

    def easy_x(self):
        self.printing()
        self.ai(self.comp_sign)

    def easy_o(self):
        self.printing()
        self.ai(self.enemy_sign)

    def fplaying(self, dict_name, x, y):
        self.breaker = 0
        while self.breaker == 0:
            dict_name[self.input][x]()
            if self.breaker == 1:
                break
            else:
                dict_name[self.input][y]()

    def playing(self):
        self.display()
        self.fplaying(self.comm, 2, 3)

    def exit(self):
        self.start = False


class Medium(Tictac):
    def __init__(self):
        super().__init__()
        self.ai_pos = None
        self.enemy_pos = None
        self.id = {0: {0: 0, 1: 1, 2: 2}, 1: {3: 3, 4: 4, 5: 5},
                   2: {6: 6, 7: 7, 8: 8}, 3: {0: 0, 3: 3, 6: 6},
                   4: {1: 1, 4: 4, 7: 7}, 5: {2: 2, 5: 5, 8: 8},
                   6: {0: 0, 4: 4, 8: 8}, 7: {6: 6, 4: 4, 2: 2}}
        self.command = {'start easy easy': {1: self.playing}, 'start easy user': {1: self.playing},
                        'start user easy': {1: self.playing}, 'start user user': {1: self.playing},
                        'exit': {1: self.exit},
                        'start medium medium': {1: self.mplaying, 2: self.medium_comp, 3: self.omedium_comp},
                        'start user medium': {1: self.mplaying, 2: self.human_x, 3: self.medium_comp},
                        'start medium user': {1: self.mplaying, 2: self.medium_comp, 3: self.human_x},
                        'start medium easy': {1: self.mplaying, 2: self.medium_comp, 3: self.easy_o},
                        'start easy medium': {1: self.mplaying, 2: self.easy_o, 3: self.medium_comp}}

    def analyzer(self):
        super().parser()
        comp_counter = [x.count(self.comp_sign) for x in self.result]  # analyzer
        enemy_counter = [x.count(self.enemy_sign) for x in self.result]
        self.ai_pos = [index for index in range(len(comp_counter)) if comp_counter[index] == 2]
        self.enemy_pos = [index for index in range(len(enemy_counter)) if enemy_counter[index] == 2]

    def medium_move(self, position, sign, info):
        print(info)
        for i in list(self.id[position[0]].values()):
            self.board_index.remove(i) if self.game_board[i] == ' ' else None
            self.game_board[i] = sign if self.game_board[i] == ' ' else self.game_board[i]
        self.display()
        self.winner()

    def analysis(self, my_position, my_sign, enemy_position):
        if my_position and ' ' in self.result[my_position[0]]:
            self.medium_move(my_position, my_sign, 'Executing winning strategic move level "medium"')
        elif enemy_position and ' ' in self.result[enemy_position[0]]:
            self.medium_move(enemy_position, my_sign, 'Executing preventative strategic move level "medium"')
        else:
            print('Making random move level "medium"')
            self.ai(my_sign)

    def medium_comp(self):
        self.analyzer()
        self.analysis(self.ai_pos, self.comp_sign, self.enemy_pos)

    def omedium_comp(self):
        self.analyzer()
        self.analysis(self.enemy_pos, self.enemy_sign, self.ai_pos)

    def mplaying(self):
        self.display()
        self.fplaying(self.command, 2, 3)


class Hard(Medium):
    def __init__(self):
        Medium.__init__(self)
        self.hcommand = {'start easy easy': {1: self.playing}, 'start easy user': {1: self.playing},
                         'start user easy': {1: self.playing}, 'start user user': {1: self.playing},
                         'exit': {1: self.exit},
                         'start medium medium': {1: self.mplaying}, 'start user medium': {1: self.mplaying},
                         'start medium user': {1: self.mplaying}, 'start medium easy': {1: self.mplaying},
                         'start easy medium': {1: self.mplaying},
                         'start hard easy': {1: self.hplaying, 2: self.hard_ai_x, 3: self.easy_o},
                         'start easy hard': {1: self.hplaying, 2: self.easy_o, 3: self.hard_ai_x},
                         'start hard medium': {1: self.hplaying, 2: self.hard_ai_x, 3: self.omedium_comp},
                         'start medium hard': {1: self.hplaying, 2: self.omedium_comp, 3: self.hard_ai_x},
                         'start hard user': {1: self.hplaying, 2: self.hard_ai_x, 3: self.human_x},
                         'start user hard': {1: self.hplaying, 2: self.human_x, 3: self.hard_ai_x},
                         'start hard hard': {1: self.hplaying, 2: self.hard_ai_x, 3: self.hard_ai_o}}

    def empty_index(self):
        return [index for index in range(len(self.game_board)) if self.game_board[index] == ' ']

    def winning(self, maxer, miner):
        rd = [''.join(x) for x in self.wincheck()]
        if maxer * 3 in rd:
            return 10
        elif miner * 3 in rd:
            return -10
        else:
            return 0

    def minimax(self, depth, isMax, playerX, playerO, alpha, beta):
        spots = self.empty_index()
        score = self.winning(playerX, playerO)

        # terminal state
        if score == 10:
            return score - depth  # making AI smarter by subtracting and adding depth for max and min player
        elif score == -10:
            return score + depth
        elif len(spots) == 0:  # checking for empty spots
            return 0

        if isMax:
            best = -1000
            for i in range(len(self.game_board)):
                if self.game_board[i] == ' ':
                    self.game_board[i] = playerX
                    best = max(best, self.minimax(depth + 1, not isMax, playerX, playerO, alpha, beta))
                    self.game_board[i] = ' '
                    if best >= beta:
                        return best
                    if best > alpha:
                        alpha = best
            return best
        else:
            best = 1000
            for i in range(len(self.game_board)):
                if self.game_board[i] == ' ':
                    self.game_board[i] = playerO
                    best = min(best, self.minimax(depth + 1, not isMax, playerX, playerO, alpha, beta))
                    self.game_board[i] = ' '
                    if best <= alpha:
                        return best
                    if best < beta:
                        beta = best
            return best

    def bestmove(self, xplayer, oplayer, isMax, alpha, beta):
        best = None
        bestval = -1000
        for i in range(len(self.game_board)):
            if self.game_board[i] == ' ':
                self.game_board[i] = xplayer
                moveval = self.minimax(0, isMax, xplayer, oplayer, alpha, beta)
                self.game_board[i] = ' '
                if moveval > bestval:
                    best = i
                    bestval = moveval
        return best

    def hard_move(self, my_sign, enemy_sign):
        print('Making move level "hard"')
        i = self.bestmove(my_sign, enemy_sign, False, -1000, 1000)
        self.game_board[i] = my_sign
        self.board_index.remove(i)
        self.display()
        self.winner()

    def hard_ai_x(self):
        self.hard_move(self.comp_sign, self.enemy_sign)

    def hard_ai_o(self):
        self.hard_move(self.enemy_sign, self.comp_sign)

    def hplaying(self):
        self.display()
        self.fplaying(self.hcommand, 2, 3)

    def pcommand(self):
        while self.start:
            self.input = input('Input command: ')
            try:
                self.psigns()
                self.hcommand[self.input][1]()
            except KeyError:
                print('Command not found, try again')


h = Hard()
h.pcommand()
