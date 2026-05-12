import numpy as np

def generateSmatrix(n: int):
    matrix = []
    for row in range(n):
        temp = []
        for column in range(n):
            if (column == (row+1)%n):
                temp.append(1)
            else:
                temp.append(0)
        matrix.append(temp)
    return np.array(matrix)

def generateImatrix(n: int):
    matrix = []
    for row in range(n):
        temp = []
        for column in range(n):
            if (row == column):
                temp.append(1)
            else:
                temp.append(0)
        matrix.append(temp)
    return np.array(matrix)

def generateEmptymatrix(l: int, m: int):
    matrix = []
    n = l*m
    for row in range(n):
        temp = []
        for column in range(n):
            temp.append(0)
        matrix.append(temp)
    return np.array(matrix)

# Finding the rank of a matrix
def gf2_rank(M):
    M = M.copy() % 2  # ensure binary
    rows, cols = M.shape
    rank = 0
    for col in range(cols):
        pivot = None
        for r in range(rank, rows):
            if M[r, col] == 1:
                pivot = r
                break
        if pivot is not None:
            # Swap pivot row to the top of the unprocessed part
            M[[rank, pivot]] = M[[pivot, rank]]
            # Eliminate other 1's in this column
            for r in range(rows):
                if r != rank and M[r, col] == 1:
                    M[r] ^= M[rank]  # XOR for mod 2 subtraction
            rank += 1
    return rank


# For TT Codes: input x, y, z values for A_1, A_2, A_3, B_1, ..., C_3