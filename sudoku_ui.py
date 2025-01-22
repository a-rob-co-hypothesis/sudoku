N=9



def sudoku_print(array):
    ci=0
    cj=0
    for i in array:
        ci+=1
        cj=0
        for j in i:
            cj+=1
            print(j, end=" ")
            if cj==N:
                print()
            elif cj%3 == 0:
                print('|', end=" ")
        if ci==3 or ci==6 :
            print('- - - | - - - | - - -')



if __name__ == '__main__':
    # Import the 'os' module to work with the operating system.
    from os import path

    # Use the 'os.path.realpath(__file__)' to get the full path of the current Python script.
    # This will print the path of the current file.
    print("Current File Name: ", path.basename(__file__))
