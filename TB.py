import numpy as np

def main():
    l = input("Enter a number (l): ")
    if (not l.isdigit() or int(l) <= 1):
        print("Not a valid number")
        return 1
    else:
        l = int(l)
    m = input("Enter a number (m): ")
    if (not m.isdigit() or int(m) <= 1):
        print("Not a valid number")
        return 1
    else:
        m = int(m)
    
    l_Smatrix = generateSmatrix(l)
    m_Smatrix = generateSmatrix(m)
    l_Imatrix = generateImatrix(l)
    m_Imatrix = generateImatrix(m)

    x = np.kron(l_Smatrix, m_Imatrix)
    y = np.kron(l_Imatrix, m_Smatrix)
    z = np.kron(l_Smatrix, m_Smatrix)
    
    xpowerA = input("(Matrix A) Enter a power for x: ")
    if (not xpowerA.isdigit() or int(xpowerA) < 0):
        print("Not a valid number")
        return 1
    else:
        xpowerA = int(xpowerA)
        
    ypowerA = input("(Matrix A) Enter a power for y: ")
    if (not ypowerA.isdigit() or int(ypowerA) < 0):
        print("Not a valid number")
        return 1
    else:
        ypowerA = int(ypowerA)
        
    zpowerA = input("(Matrix A) Enter a power for z: ")
    if (not zpowerA.isdigit() or int(zpowerA) < 0):
        print("Not a valid number")
        return 1
    else:
        zpowerA = int(zpowerA)
        
    xpowerB = input("(Matrix B) Enter a power for x: ")
    if (not xpowerB.isdigit() or int(xpowerB) < 0):
        print("Not a valid number")
        return 1
    else:
        xpowerB = int(xpowerB)
        
    ypowerB = input("(Matrix B) Enter a power for y: ")
    if (not ypowerB.isdigit() or int(ypowerB) < 0):
        print("Not a valid number")
        return 1
    else:
        ypowerB = int(ypowerB)
    
    zpowerB = input("(Matrix B) Enter a power for z: ")
    if (not zpowerB.isdigit() or int(zpowerB) < 0):
        print("Not a valid number")
        return 1
    else:
        zpowerB = int(zpowerB)
       
    Amatrix = generateEmptymatrix(l, m)
    if (xpowerA > 0):
        Axterm = x
        for _ in range(1, xpowerA):
            Axterm = np.dot(Axterm, x)
        Amatrix = np.bitwise_xor(Amatrix, Axterm)
    if (ypowerA > 0):
        Ayterm = y
        for _ in range(1, ypowerA):
            Ayterm = np.dot(Ayterm, y)
        Amatrix = np.bitwise_xor(Amatrix, Ayterm)
    if (zpowerA > 0):
        Azterm = z
        for _ in range(1, zpowerA):
            Azterm = np.dot(Azterm, z)
        Amatrix = np.bitwise_xor(Amatrix, Azterm)
    
    Bmatrix = generateEmptymatrix(l, m)
    if (xpowerB > 0):
        Bxterm = x
        for _ in range(1, xpowerB):
            Bxterm = np.dot(Bxterm, x)
        Bmatrix = np.bitwise_xor(Bmatrix, Bxterm)
    if (ypowerB > 0):
        Byterm = y
        for _ in range(1, ypowerB):
            Byterm = np.dot(Byterm, y)
        Bmatrix = np.bitwise_xor(Bmatrix, Byterm)
    if (zpowerB > 0):
        Bzterm = z
        for _ in range(1, zpowerB):
            Bzterm = np.dot(Bzterm, z)
        Bmatrix = np.bitwise_xor(Bmatrix, Bzterm)
        
    Hx = np.hstack((Amatrix, Bmatrix))
    Amatrix_transpose = Amatrix.transpose()
    Bmatrix_transpose = Bmatrix.transpose()
    Hz = np.hstack((Bmatrix_transpose, Amatrix_transpose))
    
    physical_qubits = Hx.shape[1]
    num_independent_stabilizers = gf2_rank(Hx) + gf2_rank(Hz)
    logical_qubits = physical_qubits - num_independent_stabilizers
    
    print(f"n = {physical_qubits}")
    print(f"k = {logical_qubits}")
    
    #print(f"Hx = {Hx}")
    #print(f"Hz = {Hz}")
    
    return 0
    
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

if __name__ == '__main__':
    main()