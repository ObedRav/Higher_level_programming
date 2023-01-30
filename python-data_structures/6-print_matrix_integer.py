#!/usr/bin/python3
def print_matrix_integer(matriz=[[]]):
    if (not matriz[0]):
        print()
    for i in range(len(matriz)):
        for j in matriz[i]:
            if (j == matriz[i][-1]):
                print("{:d}".format(j))
            else:
                print("{:d}".format(j), end=" ")