# Adv. AI - Assignment 2 - Sai
## Question 2
### Preparing to run
This folder consists of three python files. 
- `main.py`
- `puzzle_handler.py`
- `util.py`

All of them are required for a successful run.

> **_NOTE:_** This program contains colored text which may not appear correctly on older terminals.

> **_On Windows:_** It is recommended to use newer version of terminal which can be obtained from [here](https://apps.microsoft.com/detail/9n0dx20hk701?hl=en-US&gl=US) if not installed.

### Run
Almost all the edge cases are considered. You cannot give a wrong input puzzle. 

Just execute the following command.
```sh
python main.py
```
And follow the instructions.


### Solvability
There is puzzle solvability check that has been implemented. It counts the number of inversions present in a puzzle state, and returns true or false when certain conditions are met.

It is mostly accurate for $N = 8$ but overall not a reliable check for larger puzzles.

### Simulated Annealing
I have tested a number of scheduling functions, most of them linear, and start from $T = 100$. I played with values of $T$ between 1 and 10000. For determining boltzmann's probability, $T = 1$ worked better because $\Delta E$ is a small number. Because higher $T$ would result in a longer time to converge without much better results.
And the final scheduling function is defined as follows:
$$T = 1 - \frac{t+1}{t_{max}}$$
where $t_{max}$ represents the max number of iterations that occur before the annealing exits. $t$ counts the number of iterations and starts from 0.
So as more iterations occur, $t$ increases and $\frac{t+1}{t_{max}}$ reaches 1, when $t = t_{max} - 1$, and $T$ becomes 0, which is when annealing exits.


> **_NOTE:_** Annealing also exits early if a solution is found before $T$ reaches 0.

For acceptable $N$, 

$N < 24$, $t_{max} = 1000000$, and 

$N >= 24$, $t_{max} = \sqrt{N+1} \times 1000000$. 

So expect longer running times from $N>=24$.

The images below show different runs of annealing.

This is the example input from the Assignment 2 description on canvas.
![](images/screen1.png)
This is a random 15-puzzle.
![](images/screen2.png)
This is a random 24-puzzle.
![](images/screen3.png)
In below two random 8-puzzles, solvability check says `Unsolvable`, but it was solved anyway.
![](images/screen4.png)
![](images/screen5.png)

More example runs.
![](images/screen6.png)
![](images/screen7.png)
![](images/screen8.png)
![](images/screen9.png)

> Some of the test puzzles are taken from this [Sliding Toys](https://sliding.toys/) website.