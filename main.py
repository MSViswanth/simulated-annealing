import math
import re
import random

# Colors from blender.org - https://svn.blender.org/svnroot/bf-blender/trunk/blender/build_files/scons/tools/bcolors.py
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

answers = ['Y', 'y', 'yes', 'Yes', 'ye', 'yea', '']

def get_input_N():
    N_ = input(f"{bcolors.HEADER}Enter the value of N in [8, 100): {bcolors.ENDC}")
    if N_ == '': 
        print(f'{bcolors.OKBLUE}Using default value for N = 8.{bcolors.ENDC}')
        N_ = '8'
    try:
        N = int(N_)
    except:
        print(f"{bcolors.WARNING}Warning: Provided N value is not a number. Please try again.{bcolors.ENDC}")
        return get_input_N()
    n_ = math.sqrt(N+1)
    if N >= 8 and N<100:
        if (n_ % math.floor(n_) == 0):
            return int(n_)
            # print("valid")
        else:
            question = input(f'{bcolors.WARNING}Invalid input!!\nWould you like to correct to {math.floor(n_)**2 - 1} (default=yes) (y/n)? {bcolors.ENDC}')
            if(question in answers):
                return int(n_)
            else:
                exit(f"{bcolors.FAIL}Exiting! Please run the program again.{bcolors.ENDC}")
    else:
        print(f"{bcolors.WARNING}Warning: Invalid input!! Please input N such that 8 <= N < 100.{bcolors.ENDC}")
        return get_input_N()


# n = get_input_N()
n = 3
N_puzzle = []
N = n**2 - 1

def take_row_input(i):
    prev_list = []
    # print(f'i:{i}')
    for row_number in range(0, int(i/n)):
        prev_list.extend([item for item in N_puzzle[row_number]])
    row = input(f'{bcolors.OKBLUE}Row {int(i/n)+1}: {bcolors.ENDC}')
    row = re.findall(r'\d+', row)
    row = [int(item) for item in row]
    if len(row) == n and len(list(set(row))) < n:
        print(f"{bcolors.WARNING}Warning: Duplicates present in row.{bcolors.ENDC}")
    if len(list(set(row))) == n:
            count_unique = 0
            for j in row:
                if j <= N:
                    if(j not in prev_list):
                        count_unique+=1
                    else:
                        print(f'{bcolors.WARNING}Warning: {j} is already present in previous rows.{bcolors.ENDC}')
                else:
                    print(f'{bcolors.WARNING}Warning: Row numbers cannot be more than {N}.{bcolors.ENDC}')
            if count_unique == n:
                N_puzzle.append(row)
            else:
                print(f"{bcolors.OKBLUE}Please enter the row numbers again.{bcolors.ENDC}")
                take_row_input(i)        
    else:
        print(f'{bcolors.WARNING}Warning: Invalid number of columns. Please enter row again with {n} columns.{bcolors.ENDC}')
        take_row_input(i)

def gen_state(list):
    generated_state = []
    row_list = []
    for i, number in enumerate(list):
        if i % n == 0:
            row_list = []
            generated_state.append(row_list)
        if number == N+1:
            row_list.append(0)
        else:
            row_list.append(number)
    return generated_state

# print(f'{bcolors.OKBLUE}Building {N}-puzzle. Please enter the current state below (1 row at a time).{bcolors.ENDC}')
# for i in range(0, n**2):
#     if i % n == 0:
#         take_row_input(i)
        
goal_N_puzzle = gen_state(range(1, N+2))

N_puzzle = [[6, 4, 7], [8, 5, 0], [3, 2, 1]]
# print(N_puzzle)
# print(goal_N_puzzle)


def manhattan_distance(state_a, state_b):
    state_a_dict = {}
    state_b_dict = {}
    for i in range(0,n):
        for j in range(0,n):
            state_a_dict[state_a[i][j]] = (i, j)
            state_b_dict[state_b[i][j]] = (i, j)
    man_dist = 0
    for key in state_a_dict.keys():
        pos_a = state_a_dict[key]
        pos_b = state_b_dict[key]
        man_dist += abs(pos_a[0] - pos_b[0]) + abs(pos_a[1] - pos_b[1])
    return man_dist

dist = manhattan_distance(goal_N_puzzle, N_puzzle)

def gen_random_state():
    return gen_state(random.sample(range(1,N+2), N+1))

