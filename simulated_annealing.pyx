import copy
import math
import random
import sys
import time
import math
import random

from puzzle_handler import Puzzle_handler
from util import util



class Simulated_annealing:
    """
    Simulated_annealing class contains the heuristic which determines the value of a state, the `simulated_annealing` function that performs annealing.
    It also has a couple puzzle related functions which need to be moved.
    """
    def __init__(self) -> None:
        self.__moves = []
    
    def get_moves(self):
        """
        Returns the moves taken from initial state to reach the final state.
        """
        if self.__moves == []:
            print("Please run the simulated annealing method.")
        return self.__moves
    
    def manhattan_distance(self, state_a, state_b):
        """
        Returns manhattan distance between two puzzle states.
        """
        state_a_dict = {}
        state_b_dict = {}
        for i in range(0, len(state_a)):
            for j in range(0, len(state_a)):
                state_a_dict[state_a[i][j]] = (i, j)
                state_b_dict[state_b[i][j]] = (i, j)
        man_dist = 0
        for key in state_a_dict.keys():
            pos_a = state_a_dict[key]
            pos_b = state_b_dict[key]
            man_dist += abs(pos_a[0] - pos_b[0]) + abs(pos_a[1] - pos_b[1])
        return man_dist
    
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
    
    def possible_dir(self, state):
        """
        Returns the possible directions that the tiles can move in a given state.
        """
        state_list = self.gen_state_list(state)
        n = len(state)
        zero_pos = state_list.index(0)
        row = int(zero_pos/n)
        col = zero_pos%n
        dirs = []
        if row > 0:
            dirs.append("down")
        if col > 0:
            dirs.append("right")
        if col < n-1:
            dirs.append("left")
        if row < n-1:
            dirs.append("up")
        return dirs
    
    def move_tile(self, state: list, move):
        """
        Takes state and direction as input and moves the tile in that state and returns the updated state.
        """
        state_list = self.gen_state_list(state)
        zero_pos = state_list.index(0)
        n = len(state)
        row = int(zero_pos/n)
        col = zero_pos%n
        if move == 'down':
            state[row-1][col], state[row][col] = state[row][col], state[row-1][col]
        if move == 'up':
            state[row][col], state[row+1][col] = state[row+1][col], state[row][col]
        if move == 'right':
            state[row][col], state[row][col-1] = state[row][col-1], state[row][col]
        if move == 'left':
            state[row][col+1], state[row][col] = state[row][col], state[row][col+1]
        return state

    def simuluated_annealing(self,initial_state, goal_state):
        """
        Performs simulated annealing. Takes initial state and the goal state.
        """
        current_state:list = initial_state
        n = len(current_state)
        t = 0
        count = 0
        T = 1
        if n < 5:
            t_max = 1000000
        else:
            t_max = n * 1000000
        while T > 0:
            alpha = (t+1)/t_max
            t += 1
            T = 1 - alpha
            print(f'{util.OKBLUE} Annealing...{util.animation[int(alpha*10)]} {round(alpha*100, 1)} %{util.ENDC}', end="\r", flush=True)
            current_value = self.manhattan_distance(current_state, goal_state)
            if T == 0 or current_value == 0:
                if T == 0:
                    print(f'{util.OKBLUE}\n Annealing finished.{util.ENDC}')
                elif current_value == 0:
                    print(f'{util.OKBLUE}\n Annealing stopped. Reached goal early.{util.ENDC}')
                return count, t, current_state
            next_dirs = self.possible_dir(current_state)
            # print(next_dirs)
            dir = random.choice(next_dirs)
            copy_current = copy.deepcopy(current_state)
            next_state = self.move_tile(copy_current, dir)
            next_value = self.manhattan_distance(next_state, goal_state)
            delta_e = current_value - next_value
            # print(delta_e)
            if delta_e > 0:
                current_state = next_state
                self.__moves.append(dir)
                count += 1
            else:
                rand = random.random()
                boltzman_prob = math.exp((delta_e)/T)
                if rand < boltzman_prob:
                    current_state = next_state
                    self.__moves.append(dir)
                    count += 1







# if(sim_ann.manhattan_distance(result, goal_N_puzzle) ==0):
#     puzzle_q = input(f"{util.WARNING}Would you like to see the steps taken to get to the goal (y/n) (default=y): {util.ENDC}")
#     if puzzle_q in util.answers:
#         steps = sim_ann.get_moves()
#         print('\n'*n)
#         for step in steps:
#             for _ in range(n):
#                 sys.stdout.write("\x1b[1A")  # cursor up one line
#                 sys.stdout.write("\x1b[2K") 
#                 time.sleep(0.0001)
#             puzzle_handler.print_puzzle(sim_ann.move_tile(N_puzzle, step))
            
