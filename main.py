import math



answers = ['Y', 'y', 'yes', 'Yes', 'ye', 'yea']

def get_input_N():
    N = int(input("Enter the value of N [8, 100): "))

    n_ = math.sqrt(N+1)
    if N >= 8 and N<100:
        if (n_ % math.floor(n_) == 0):
            return int(n_)
            # print("valid")
        else:
            question = input(f'Invalid input!!\nDo you want to correct it to {math.floor(n_)**2 - 1} (y/n)? ')
            if(question in answers):
                return int(n_)
            else:
                exit("Exiting! Please run the program again.")
    else:
        print("Invalid input!! Please input N such that 8 <= N < 100")
        return get_input_N()


n = get_input_N()
print(n)