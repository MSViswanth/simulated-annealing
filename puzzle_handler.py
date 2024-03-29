import random
import re
from util import util
import math

class Puzzle_handler:
    """
    Puzzle_handler handles various puzzle related stuff. Initializing this object should allow it take the input N-puzzle.
    The inputs are made available via `get_puzzle_params` method.
    """
    def __init__(self) -> None:
        self.__n = self.__get_input_N()
        self.__N = self.__n**2 - 1
        self.__N_puzzle = []
        self.__take_input()
        self.__goal_N_puzzle = self.gen_state(range(1, self.__N+2))

    def __take_input(self):
        """
        Receives the input N-puzzle state.
        """
        __gen_q = input(f'{util.OKBLUE}Would you like to generate an initial random state (y/n) (default=y): {util.ENDC}')
        if __gen_q in util.answers:
            self.__N_puzzle = self.gen_random_state(self.__N)
            print(f'{util.OKBLUE}Successfully built random {self.__N}-puzzle.{util.ENDC}')
            self.print_puzzle(self.__N_puzzle)
        else:
            print(f'{util.OKBLUE}Building {
                self.__N}-puzzle. Please enter the current state below (1 row at a time).{util.ENDC}')
            for i in range(0, self.__n**2):
                if i % self.__n == 0:
                    self.__take_row_input(i)
    
    def get_puzzle_params(self):
        """
        Returns size of the puzzle `n`, `N`, and input N-puzzle, and the goal N-puzzle.

        Eg. For N = 8, n = 3
        """
        return self.__n, self.__N, self.__N_puzzle, self.__goal_N_puzzle
    
    def is_solvable(self, state):
        """
        Checks if a given N-puzzle state is solvable.
        """
        inversions = 0
        state_list = self.gen_state_list(state)
        for i in range(0, len(state_list)):
            for j in range(i+1, len(state_list)):
                if(state_list[i] > state_list[j]):
                    if state_list[j] != 0:
                        inversions+=1
        # for i in range(0, len(state)):
        #     for j in range(0, len(state)-1):
        #         if(state[i][j] > state[i][j+1]):
        #             if state[i][j+1] != 0:
        #                 inversions+=1
        # for i in range(0, len(state)-1):
        #     for j in range(0, len(state)):
        #         if(state[i][j] > state[i+1][j]):
        #             if state[i+1][1] != 0:
        #                 inversions+=1
        if len(state) % 2 != 0:
            return inversions % 2 == 0
        else:
            zero_pos = state_list.index(0)
            row = int(zero_pos / len(state))
            return row % 2 == 0


    def __get_input_N(self):
        """
        Receives the input `N`.
        """
        N_ = input(f"{util.HEADER}Enter the value of N in [8, 100) (default=8): {
                util.ENDC}")
        if N_ == '':
            N_ = '8'
        try:
            N = int(N_)
        except:
            print(f"{util.WARNING}Warning: Provided N value is not a number. Please try again.{
                util.ENDC}")
            return self.__get_input_N()
        n_ = math.sqrt(N+1)
        if N >= 8 and N < 100:
            if (n_ % math.floor(n_) == 0):
                return int(n_)
            else:
                question = input(f'{util.WARNING}Invalid input!!\nWould you like to correct to {
                                math.floor(n_)**2 - 1} (y/n) (default=y)? {util.ENDC}')
                if (question in util.answers):
                    return int(n_)
                else:
                    exit(f"{util.FAIL}Exiting! Please run the program again.{util.ENDC}")
        else:
            print(f"{util.WARNING}Warning: Invalid input!! Please input N such that 8 <= N < 100.{
                util.ENDC}")
            return self.__get_input_N()


    def __take_row_input(self, i):
        """
        Receives and processes the input given in a row.
        """
        prev_list = []
        # print(f'i:{i}')
        for row_number in range(0, int(i/self.__n)):
            prev_list.extend([item for item in self.__N_puzzle[row_number]])
        row = input(f'{util.OKBLUE}Row {int(i/self.__n)+1}: {util.ENDC}')
        row = re.findall(r'\d+', row)
        row = [int(item) for item in row]
        if len(row) == self.__n and len(list(set(row))) < self.__n:
            print(f"{util.WARNING}Warning: Duplicates present in row.{util.ENDC}")
        if len(list(set(row))) == self.__n:
            count_unique = 0
            for j in row:
                if j <= self.__N:
                    if (j not in prev_list):
                        count_unique += 1
                    else:
                        print(f'{util.WARNING}Warning: {
                            j} is already present in previous rows.{util.ENDC}')
                else:
                    print(f'{util.WARNING}Warning: Row numbers cannot be more than {
                        self.__N}.{util.ENDC}')
            if count_unique == self.__n:
                self.__N_puzzle.append(row)
            else:
                print(f"{util.OKBLUE}Please enter the row numbers again.{util.ENDC}")
                self.__take_row_input(i)
        else:
            print(f'{util.WARNING}Warning: Invalid number of columns. Please enter row again with {
                self.__n} columns.{util.ENDC}')
            self.__take_row_input(i)
    
    def gen_state(self, state_list):
        """
        Takes a `state list` and returns an N-puzzle `state`.
        """
        generated_state = []
        row_list = []
        for i, number in enumerate(state_list):
            if i % self.__n == 0:
                row_list = []
                generated_state.append(row_list)
            if number == self.__n**2:
                row_list.append(0)
            else:
                row_list.append(number)
        return generated_state
    
    def gen_state_list(self, state):
        """
        Takes an N-puzzle `state` as input and returns a `state list`.
        """
        state_list = []
        for number in state:
            state_list.extend(number)
        return state_list
    
    def gen_random_state(self, N):
        """
        Takes `N` as input and returns a random `state` for the N-puzzle.
        """
        return self.gen_state(random.sample(range(1, N+2), N+1))

    def print_puzzle(self,*args):
        """
        Takes one or two N-puzzle states as input and prints them on to the terminal.
        """
        title = ['Initial', 'Final']
        n = len(args[0])
        if (len(args) == 2):
            print(
                f'{{:^{n*3}s}} {{:<{n*3}s}} {{:^{n*3}s}}'.format(title[0], '', title[1]))
            for i in range(0, n):
                for k, arg in enumerate(args):
                    # print(arg)
                    for j in range(0, n):
                        print('{:>2d}'.format(arg[i][j]), end=' ')
                    print(f'{{:<{n*3}s}}'.format(''), end=' ')
                print('')
        elif len(args) == 1:
            print('\r', end='\r')
            for i in range(0, n):
                for j in range(0, n):
                    print('{:>2d}'.format(args[0][i][j]), end=' ')
                print('')