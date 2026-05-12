import numpy as np
import utils 
from utils import generateSmatrix, generateImatrix

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
    p = input("Enter a number (p): ")
    if (not p.isdigit() or int(p) <= 1):
        print("Not a valid number")
        return 1
    
    l_Smatrix = generateSmatrix(l)
    m_Smatrix = generateSmatrix(m)
    p_Smatrix = generateSmatrix(p)
    l_Imatrix = generateImatrix(l)
    m_Imatrix = generateImatrix(m)
    p_Imatrix = generateImatrix(p)
    
    x = np.kron(np.kron(l_Smatrix, m_Imatrix), p_Imatrix)
    y = np.kron(np.kron(l_Imatrix, m_Smatrix), p_Imatrix)
    z = np.kron(np.kron(l_Imatrix, m_Imatrix), p_Smatrix)
    
    # A = A_1 + A_2 + A_3 
    # B = B_1 + B_2 + B_3
    # C = C_1 + C_2 + C_3
    # e.g. A = 1 + y^2 + xy^2z 
    
    

    
    
if __name__ == "__main__":
    main()