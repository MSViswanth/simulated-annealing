import math
import random
import time
import math
import random

from puzzle_handler import Puzzle_handler
from util import util



class Simulated_annealing:
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





    def simuluated_annealing(self,initial_state, goal_state):
        """
        Performs simulated annealing.
        """
        current = initial_state
        n = len(current)
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
            print(f'{util.OKBLUE}Annealing...{
                util.animation[int(alpha*10)]} {round(alpha*100, 2)} %{util.ENDC}', end="\r")
            current_value = self.manhattan_distance(current, goal_state)
            if T == 0 or current_value == 0:
                print(f'{util.OKBLUE}\nAnnealing successful.{util.ENDC}')
                return count, t, current
            next = puzzle_handler.gen_random_state(N)
            next_value = self.manhattan_distance(next, goal_state)
            delta_e = current_value - next_value
            if delta_e > 0:
                current = next
                count += 1
            else:
                rand = random.random()
                boltzman_prob = math.exp((delta_e)/T)
                if rand < boltzman_prob:
                    current = next
                    count += 1
        return count, t, current




puzzle_handler = Puzzle_handler()

_, N, N_puzzle, goal_N_puzzle = puzzle_handler.get_puzzle_params()

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
