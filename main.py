#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ISAT 690
Summer 2022
Assignment #1 - Second Moment Matrix
@Author: Jenna Dauzat
"""
import numpy as np

def get_input_image_matrix():
    input_image = np.array([
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 50, 60, 60, 60, 60, 60, 10, 10],
        [10, 10, 50, 60, 60, 60, 60, 60, 10, 10],
        [10, 10, 50, 50, 10, 10, 10, 10, 10, 10],
        [10, 10, 50, 50, 10, 10, 10, 10, 10, 10],
        [10, 10, 50, 50, 10, 10, 10, 10, 10, 10],
        [10, 10, 50, 50, 10, 10, 10, 10, 10, 10],
        [10, 10, 50, 50, 10, 10, 10, 10, 10, 10]
    ])

    return input_image

def compute_x_gradient(img, shape, *args):
    x_gradient = np.zeros(shape, np.int)
    #tuple index, value
    for idx, x in np.ndenumerate(img):
        try:
            x_gradient[idx] = img[idx[0], idx[1]+1] - img[idx]
        except IndexError:
            if args:
                expanded_window = args[0]
                x_gradient[idx] = expanded_window[idx[0], idx[1]+1] - img[idx]
            else:
                # for edges, use 0 padding as the value to the right
                x_gradient[idx] = 0 - img[idx]
    print_matrix(x_gradient)

    return x_gradient

def compute_y_gradient(img, shape, *args):
    y_gradient = np.zeros(shape, np.int)
    #tuple index, value
    for idx, x in np.ndenumerate(img):
        try:
            y_gradient[idx] = img[idx[0]+1, idx[1]] - img[idx]
        except IndexError:
            if args:
                expanded_window = args[0]
                y_gradient[idx] = expanded_window[idx[0]+1, idx[1]] - img[idx]
            else:
                #for edges, use 0 padding as the value to the right
                y_gradient[idx] = 0 - img[idx]
    print_matrix(y_gradient)

    return y_gradient

def print_matrix(matrix):
    for r in matrix:
        for c in r:
            print(c, end=" ")
        print()

def compute_second_moment_matrix(coords, img):
    x = coords[0]
    y = coords[1]
    region = np.array([[img[y-1][x-1], img[y-1][x], img[y-1][x+1]],
                       [img[y][x-1], img[y][x], img[y][x+1]],
                       [img[y+1][x-1], img[y+1][x], img[y+1][x+1]]])
    expanded_x = np.array([[img[y-1][x-1], img[y-1][x], img[y-1][x+1], img[y-1][x+2]],
                       [img[y][x-1], img[y][x], img[y][x+1], img[y][x+2]],
                       [img[y+1][x-1], img[y+1][x], img[y+1][x+1], img[y+1][x+2]]])
    expanded_y = np.array([[img[y-1][x-1], img[y-1][x], img[y-1][x+1]],
                       [img[y][x-1], img[y][x], img[y][x+1]],
                       [img[y+1][x-1], img[y+1][x], img[y+1][x+1]],
                       [img[y+2][x-1], img[y+2][x], img[y+2][x+1]]])
    print("3x3 region for pixel ({},{})".format(x,y))
    print(region)
    print("x gradient for 3x3 region with center point({},{})".format(x, y))
    ix = compute_x_gradient(region, (3,3), expanded_x)
    print("y gradient for 3x3 region with center point({},{})".format(x, y))
    iy = compute_y_gradient(region, (3,3), expanded_y)
    ix2 = np.square(ix)
    print("ix^2 = ")
    print(ix2)
    iy2 = np.square(iy)
    print("iy^2 = ")
    print(iy2)
    ixiy = np.multiply(ix, iy)
    print("ixiy = ")
    print(ixiy)
    m = np.array([[np.sum(ix2), np.sum(ixiy)],
                  [np.sum(ixiy), np.sum(iy2)]])
    print("second moment matrix for pixel({},{})".format(x,y))
    print(m)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_img = get_input_image_matrix()
    print("input image matrix: ")
    print_matrix(input_img)
    print()
    print("img gradient wrt x: ")
    imgx = compute_x_gradient(input_img.copy(), (10,10))
    print()
    print("img gradient wrt y: ")
    imgy = compute_y_gradient(input_img.copy(), (10,10))
    print()
    #compute M matrix for these pixels in the img array
    second_moment_pixels = np.array([[2,3],
                                     [2,7],
                                     [3,4],
                                     [5,6],
                                     [6,3]])
    for r in second_moment_pixels:
        compute_second_moment_matrix(r, input_img.copy())
        print()