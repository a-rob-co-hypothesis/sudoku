
import cv2
import numpy as np
from numpy.ma.extras import average

from sudoku_solver import sudoku_solve, sudoku_check

saved_img=np.zeros((10,50,50,3),int)
for i in range(1,10):
    saved_img[i] = cv2.imread('savedImage_'+str(i)+'.png')



# def draw_rectangle:
gr=np.zeros((9,9),int)
#print(gr)

def sudoku_scan(img_name,show=False):

    img = cv2.imread(img_name)
    img = cv2.resize(img, (220*4, 220*4))

    #remove grey with threshold
    black=1
    threshold=127
    if black:
        (tr,img) = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

    i_b,i_w=0,0
    j_b,j_w,j_0=0,0,0
    for line in range(9):
        if line == 0:
            while i_b < len(img) and img[i_b, i_b, 0] != 255:
                i_b += 1
            j_b=i_b
            j_0=j_b
        else:
            j_b=j_0
            while i_b < len(img) and img[i_b, j_b, 0] != 255:
                i_b += 1
        i_w=i_b

        while i_w < len(img) and img[i_w, j_b, 0] == 255:
            i_w += 1

        for col in range(9):
            if col>0:
                j_b=j_w
                while j_b < len(img) and img[i_b, j_b, 0] != 255:
                    j_b += 1
            j_w=j_b
            while j_w < len(img) and img[i_b, j_w, 0] == 255:
                j_w += 1

            gr[line,col] = np.average(img[i_b:i_w, j_b:j_w, 0])
            start_point = (j_b, i_b)
            end_point = (j_w, i_w)
            color = (0, 0, 255)
            img = cv2.rectangle(img, start_point, end_point, color)
            #print( (line,col), start_point, end_point, (end_point[0] -start_point[0],end_point[1] -start_point[1]) )
            if gr[line,col] <250:
                up,down,left,right=0,0,0,0
                for p in range(j_b + 1, j_w):
                    # print(int(0 in (img[i_b + 1:i_w, p, 0])), end=' ')
                    if (not left) and 0 in img[i_b + 1:i_w, p, 0]:
                        left = p
                    if left and (not right) and 0 not in img[i_b + 1:i_w, p, 0]:
                        right = p
                # print()
                for p in range(i_b + 1, i_w):
                    # print(int(0 in (img[p, j_b + 1:j_w, 0])), end=' ')
                    if (not up) and 0 in img[p, j_b + 1:j_w, 0]:
                        up = p
                    if up and (not down) and 0 not in img[p, j_b + 1:j_w, 0]:
                        down = p

                # print()
                #print(up-down,left-right)
                start_point = (left-2, up-2)
                end_point = (right+1, down+1)
                color = (0, 0, 255)
                img = cv2.rectangle(img, start_point, end_point, color)
                gr[line, col] = predict(img[up:down, left:right, 0])
            else:
                gr[line, col] = 0
    #print(gr)

    # img[i:i + 10, i] = [0, 0, 255]
    # img[i:i + 10, i+10] = [0, 0, 255]
    # img[i, i:i+10] = [0, 0, 255]
    # img[i +10, i:i + 10] = [0, 0, 255]
    # print(i, j, shape(img[i:i + skip_v, j:j + skip_h, 0]), av)

    if show:
        # Display the image
        cv2.imshow("Image", img)#[0:120,0:int(220/9)])
        # Wait for the user to press a key
        cv2.waitKey(0)
        # Close all windows
        cv2.destroyAllWindows()
        #print(img.shape)
    return gr


dico_av={137:1,152:2,157:3,153:4,151:5,139:6,172:7,130:8,140:9}
a=0



def predict(cell):

    cell = cv2.resize(cell,(50,50) )
    (tr, cell) = cv2.threshold(cell, 127, 255, cv2.THRESH_BINARY)
    ar=np.zeros(9)
    for i in range(9):
        cell_i= np.copy(cell)
        cell_i[:]=((cell[:]!=saved_img[i+1,:,:,0])*255)

        ar[i]=np.sum(cell_i/255)

        #cv2.imshow("cell"+str(i), cell_i)
        #cv2.waitKey(1)


    p=np.argmin(ar)+1

    return p


def number_img_define(img,val):
    filename = 'savedImage_'+str(val)+'.png'
    cv2.imwrite(filename, img)
    print(str(val)+' saved to '+filename)


if __name__ == '__main__':
    # Import the 'os' module to work with the operating system.
    from os import path
    from sudoku_ui import sudoku_print

    # Use the 'os.path.realpath(__file__)' to get the full path of the current Python script.
    # This will print the path of the current file.
    print("Current File Name: ", path.basename(__file__))

    #s= input()
    #print('input =',s)

    grid_1 = sudoku_scan('sudoku_1.png',show=True)
    sudoku_print(grid_1)
    print()
    # print(list(dico_av.keys()))

    #-------------------------------------------------

    solution = sudoku_solve(grid_1)
    sudoku_print(solution)
    print ('The grid is :', sudoku_check(solution))

