from puzzle_handler import Puzzle_handler
import simulated_annealing as sim_ann
from util import util
import time

puzzle_handler = Puzzle_handler()
sim_ann2 = sim_ann.Simulated_annealing()

n, N, N_puzzle, goal_N_puzzle = puzzle_handler.get_puzzle_params()

print(f'{util.OKBLUE}Solvability check...{util.ENDC} {util.WARNING}(Unreliable): {util.ENDC}', end='')
if puzzle_handler.is_solvable(N_puzzle):
    print(f"{util.OKGREEN}Solvable! :){util.ENDC}")
else:
    print(f'{util.FAIL}Unsolvable. :({util.ENDC}')


start = time.time()
count, t, final = sim_ann2.simuluated_annealing(initial_state=N_puzzle, goal_state=goal_N_puzzle)
end = time.time()
puzzle_handler.print_puzzle(N_puzzle, final)

output_data = [
    ['Value of initial state', sim_ann2.manhattan_distance(N_puzzle, goal_N_puzzle)],
    ['Value of final state', sim_ann2.manhattan_distance(final, goal_N_puzzle)],
    ['Steps (next state is chosen)', count],
    ['Total times looped', t],
    ['Time taken for Annealing', f'{round(end-start, 2)} sec']
]

for item in output_data:
    print(f'{util.OKGREEN}{{:<30s}} : {{:<2s}}{util.ENDC}'.format(item[0], str(item[1])))