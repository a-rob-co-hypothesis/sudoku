# This is a sample Python script.
from operator import countOf

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time

from sudoku_images import sudoku_scan
from sudoku_solver import sudoku_solve, sudoku_check
from sudoku_ui import sudoku_print

N=9


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # ts stores the time in seconds
    t0= time.time()
    # print the current timestamp
    print('t=',time.time()-t0,'\n')

    # print('end')
    grid_1 = sudoku_scan('sudoku_1.png')
    sudoku_print(grid_1)
    print()
    # print(list(dico_av.keys()))
    print('t=',time.time()-t0,'\n')


    solution = sudoku_solve(grid_1)
    sudoku_print(solution)
    print('The grid is :', sudoku_check(solution))

    print('t=',time.time()-t0,'\n')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
