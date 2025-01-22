import numpy as np

from sudoku_ui import sudoku_print

N=9

grid_1=np.array([
    [0, 0, 0, 0, 5, 0, 0, 0, 7],
    [0, 0, 6, 8, 0, 0, 0, 0, 2],
    [0, 3, 0, 0, 0, 0, 9, 4, 0],

    [8, 4, 7, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 2, 5, 8],

    [0, 2, 5, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 6, 3, 0, 0],
    [3, 0, 0, 0, 8, 0, 0, 0, 0]
])

grid_1_solved=np.array([
    [4, 1, 2, 9, 5, 3, 6, 8, 7],
    [9, 7, 6, 8, 4, 1, 5, 3, 2],
    [5, 3, 8, 2, 6, 7, 9, 4, 1],

    [8, 4, 7, 3, 2, 5, 1, 6, 9],
    [2, 5, 1, 6, 9, 8, 4, 7, 3],
    [6, 9, 3, 7, 1, 4, 2, 5, 8],

    [7, 2, 5, 4, 3, 9, 8, 1, 6],
    [1, 8, 9, 5, 7, 6, 3, 2, 4],
    [3, 6, 4, 1, 8, 2, 7, 9, 5]
])


def sudoku_check(array,prints=False):
    check = True
    #print(array[0][0])
    '''for i in range(N):
        print(array[i][0], end=" ")
    print()
    for j in range(N):
        print(array[0][j], end=" ")

    print()
    print(array[0][:])'''
    print() if prints else 0
    for i in range(N):
        #horizontal:
        print(array[i, :], end=" ") if prints else 0
        #print(type(array[i, :]), end=" ")
        v=len(array[i, :]) == len(set(array[i, :]))
        print(v, end=" ") if prints else 0
        check &=v

        #vertical:
        print(array[:, i], end=" ") if prints else 0
        #print(type(array[:, i]), end=" ")
        v=len(array[:, i]) == len(set(array[:, i]))
        print(v, end=" ") if prints else 0
        check &=v


        #box:
        j=i%3*3
        k=int(i/3)*3
        box=np.concatenate((array[k, j:3+j], array[k+1, j:3+j], array[k+2, j:3+j]), axis=0)
        print(box, end=" ") if prints else 0
        #print(i,j,k)
        v=len(box) == len(set(box))
        print(v) if prints else 0
        check &=v

        if i%3==2:
            print() if prints else 0

    return check


def sudoku_solve(array):

    #init
    array3d = np.zeros((N,N,N),int)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if array[i,j] in (0,k+1):
                    array3d[i,j,k]=k+1

    #loop
    loop=0
    while(loop<10):
        #remove options:
        for i in range(N):
            for j in range(N):
                k=array[i,j]
                if k:
                    for l in range(N):
                        if i!=l :#and j!=m:
                            array3d[l,j,k-1]=0
                            #print(array3d[l,j],i,j,array[i,j]) if l==0 and j==0 else 0
                        if j!=l :
                            array3d[i, l, k - 1] = 0
                        if i!=int(i/3)*3+int(l/3) and j!=int(j/3)*3+int(l%3):
                            array3d[int(i/3)*3+int(l/3), int(j/3)*3+int(l%3), k - 1] = 0

        #remove unique
        for i in range(N):
            for j in range(N):
                if array[i, j]==0:
                    for k in range(N):
                        if array3d[i,j,k]:
                            h= array3d[i,:,k]#.count_nonzero(k+1)
                            v= array3d[:,j,k]
                            b=np.concatenate(array3d[int(i/3)*3:int(i/3)*3+3,int(j/3)*3:int(j/3)*3+3,k])
                            if np.count_nonzero(h==k+1) ==1 or np.count_nonzero(v==k+1)==1 or np.count_nonzero(b==k+1)==1:
                                array3d[i, j, :]=0
                                array3d[i, j, k]=k+1
                                #print(array3d[i, j])



        #align grid
        for i in range(N):
            for j in range(N):
                k = array[i, j]
                if k==0 and len(set(array3d[i,j]))==2:
                    array[i, j]=max(array3d[i,j])


        #print()
        #sudoku_print(array)
        loop+=1
        #print(loop)

    #print()
    #sudoku_print(array3d)
    #print(sudoku_check(array))
    return array



if __name__ == '__main__':
    # Import the 'os' module to work with the operating system.
    from os import path

    # Use the 'os.path.realpath(__file__)' to get the full path of the current Python script.
    # This will print the path of the current file.
    print("Current File Name: ", path.basename(__file__))


    solution = sudoku_solve(grid_1)
    sudoku_print(solution)
    print ('The grid is :', sudoku_check(solution))