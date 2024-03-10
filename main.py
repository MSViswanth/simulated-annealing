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
    def __init__(self) -> None:
        self.__moves = []
    
    def get_moves(self):
        if self.__moves == []:
            print("Please run simulated annealing.")
        return self.__moves
    
    def manhattan_distance(self, state_a, state_b):
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
    
    def possible_dir(self, state):
        state_list = puzzle_handler.gen_list(state)
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
        state_list = puzzle_handler.gen_list(state)
        zero_pos = state_list.index(0)
        n = len(state)
        row = int(zero_pos/n)
        col = zero_pos%n
        match move:
            case 'down':
                state[row-1][col], state[row][col] = state[row][col], state[row-1][col]
            case 'up':
                state[row][col], state[row+1][col] = state[row+1][col], state[row][col]
            case 'right':
                state[row][col], state[row][col-1] = state[row][col-1], state[row][col]
            case 'left':
                state[row][col+1], state[row][col] = state[row][col], state[row][col+1]
        return state

    def simuluated_annealing(self,initial_state, goal_state):
        """
        Performs simulated annealing.
        """
        current_state:list = initial_state
        n = len(current_state)
        N = n**2 - 1
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
            print(f'{util.OKBLUE} Annealing...{util.animation[int(alpha*10)]} {round(alpha*100, 2)} %{util.ENDC}', end="\r", flush=True)
            current_value = self.manhattan_distance(current_state, goal_state)
            if T == 0 or current_value == 0:
                print(f'{util.OKBLUE}\n Annealing finished.{util.ENDC}')
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




puzzle_handler = Puzzle_handler()

n, N, N_puzzle, goal_N_puzzle = puzzle_handler.get_puzzle_params()

print(f'{util.WARNING}Checking for solvability... (Unreliable for N >= 15): {util.ENDC}', end='')
if puzzle_handler.is_solvable(N_puzzle):
    print(f"{util.OKGREEN}Solvable! :){util.ENDC}")
else:
    print(f'{util.FAIL}Unsolvable. :({util.ENDC}')
sim_ann = Simulated_annealing()

start = time.time()
count, t, result = sim_ann.simuluated_annealing(initial_state=N_puzzle, goal_state=goal_N_puzzle)
end = time.time()
puzzle_handler.print_puzzle(N_puzzle, result)

output_data = [
    ['Value of initial state', sim_ann.manhattan_distance(N_puzzle, goal_N_puzzle)],
    ['Value of final state', sim_ann.manhattan_distance(result, goal_N_puzzle)],
    ['Steps (next state is chosen)', count],
    ['Total times looped', t],
    ['Time taken for SA', f'{round(end-start, 2)} sec']
]

for item in output_data:
    print(f'{util.OKGREEN}{{:<30s}} : {{:<2s}}{
          util.ENDC}'.format(item[0], str(item[1])))



if(sim_ann.manhattan_distance(result, goal_N_puzzle) ==0):
    puzzle_q = input(f"{util.WARNING}Would you like to see the steps taken to get to the goal (y/n) (default=y): {util.ENDC}")
    if puzzle_q in util.answers:
        steps = sim_ann.get_moves()
        # steps.reverse()
        print('\n'*n)
        for step in steps:
            for _ in range(n):
                sys.stdout.write("\x1b[1A")  # cursor up one line
                sys.stdout.write("\x1b[2K") 
                time.sleep(0.0001)
            puzzle_handler.print_puzzle(sim_ann.move_tile(N_puzzle, step))
            
