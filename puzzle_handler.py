import random
import re
from util import util
import math

class Puzzle_handler:
    def __init__(self) -> None:
        self.__n = self.__get_input_N()
        self.__N = self.__n**2 - 1
        self.__N_puzzle = []
        self.__take_input()
        self.__goal_N_puzzle = self.gen_state(range(1, self.__N+2))

    def __take_input(self):
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
        return self.__n, self.__N, self.__N_puzzle, self.__goal_N_puzzle
    
    def is_solvable(self, state):
        state_list = self.gen_list(state)
        inversions = 0
        for i in range(0, len(state_list)):
            for j in range(0, len(state_list)):
                if(state_list[i] > state_list[j]):
                    if state_list[j] != 0:
                        inversions+=1
        if inversions % 2 == 0:
            return True
        else:
            return False


    def __get_input_N(self):
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
    
    def gen_list(self, state):
        gen_list = []
        for i, number in enumerate(state):
            gen_list.extend(number)
        return gen_list
    
    def gen_random_state(self, N):
        """
        Gets random state for the N-puzzle.
        """
        return self.gen_state(random.sample(range(1, N+2), N+1))

    def print_puzzle(self,*args):
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