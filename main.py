import math
import re

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

answers = ['Y', 'y', 'yes', 'Yes', 'ye', 'yea']

def get_input_N():
    N_ = input("Enter the value of N in [8, 100): ")
    if N_ == '': 
        print(f'{bcolors.OKBLUE}Using default value for N = 8.{bcolors.ENDC}')
        N_ = '8'
    N = int(N_)
    n_ = math.sqrt(N+1)
    if N >= 8 and N<100:
        if (n_ % math.floor(n_) == 0):
            return int(n_)
            # print("valid")
        else:
            question = input(f'{bcolors.WARNING}Invalid input!!\nDo you want to correct it to {math.floor(n_)**2 - 1} (y/n)? {bcolors.ENDC}')
            if(question in answers):
                return int(n_)
            else:
                exit(f"{bcolors.FAIL}Exiting! Please run the program again.{bcolors.ENDC}")
    else:
        print("Invalid input!! Please input N such that 8 <= N < 100")
        return get_input_N()


n = get_input_N()
n_puzzle = []
N = n**2 - 1

def take_row_input(i):
    prev_list = []
    # print(f'i:{i}')
    for row_number in range(0, int(i/n)):
        prev_list.extend([item for item in n_puzzle[row_number]])
    row = input(f'Row {int(i/n)+1}: ')
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
                        # take_row_input(i)
                else:
                    print(f'{bcolors.WARNING}Warning: Row numbers cannot be more than {N}.{bcolors.ENDC}')
            if count_unique == n:
                n_puzzle.append(row)
            else:
                print(f"{bcolors.OKBLUE}Please enter the row numbers again.{bcolors.ENDC}")
                take_row_input(i)        
    else:
        print(f'{bcolors.WARNING}Warning: Invalid number of columns. Please enter row again with {n} columns.{bcolors.ENDC}')
        take_row_input(i)

print(f'{bcolors.OKBLUE}Building {N}-puzzle. Please enter the current state below (1 row at a time).{bcolors.ENDC}')
for i in range(0, n**2):
    if i % n == 0:
        take_row_input(i)
            

print(n_puzzle)