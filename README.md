# QLDPC

A Python toolkit for experimenting with **Quantum Low-Density Parity-Check (qLDPC)** codes. Currently implements two bivariate/trivariate bicycle code constructions.

## Background

qLDPC codes are a class of quantum error-correcting codes with sparse parity-check matrices. They are promising candidates for fault-tolerant quantum computing due to their favorable encoding rate and low check weight. This repo implements generator tools based on recent constructions in the literature.

## Code Constructions

### Trivariate Bicycle (TB) Codes — `TB.py`

Based on [arXiv:2507.09690](https://arxiv.org/abs/2507.09690).

Constructs a CSS code over a two-dimensional cyclic group Z_l × Z_m. The generators are:

```
x = S_l ⊗ I_m
y = I_l ⊗ S_m
z = S_l ⊗ S_m
```

where `S_n` is the cyclic shift matrix of size n and `I_n` is the identity. The parity-check matrices are:

```
Hx = [A | B]
Hz = [B^T | A^T]
```

where A and B are polynomials in x, y, z specified by the user. The tool outputs the code parameters **n** (physical qubits) and **k** (logical qubits).

**Usage:**

```bash
python TB.py
```

You will be prompted for:
- `l`, `m` — dimensions of the cyclic group (both must be > 1)
- Powers of x, y, z for matrix **A** (set a power to 0 to omit that term)
- Powers of x, y, z for matrix **B**

**Example — [[72, 12, 6]] code** (set l=6, m=6, A = x³ + y + y², B = y³ + x + x²):

```
Enter a number (l): 6
Enter a number (m): 6
(Matrix A) Enter a power for x: 3
(Matrix A) Enter a power for y: 1
(Matrix A) Enter a power for z: 0
(Matrix B) Enter a power for x: 1
(Matrix B) Enter a power for y: 3
(Matrix B) Enter a power for z: 0
n = 72
k = 12
```

---

### Trivariate Tricycle (TT) Codes — `TT.py`

Based on [arXiv:2508.08191](https://arxiv.org/abs/2508.08191).

Generalizes the BB code construction to a three-dimensional cyclic group Z_l × Z_m × Z_p. The generators are:

```
x = S_l ⊗ I_m ⊗ I_p
y = I_l ⊗ S_m ⊗ I_p
z = I_l ⊗ I_m ⊗ S_p
```

> **Status:** Work in progress. Matrix construction for A, B, C and code parameter computation are not yet implemented.

---

## Shared Utilities — `utils.py`

| Function | Description |
|---|---|
| `generateSmatrix(n)` | n×n cyclic shift matrix (permutation matrix for x → x+1 mod n) |
| `generateImatrix(n)` | n×n identity matrix |
| `generateEmptymatrix(l, m)` | lm×lm zero matrix |
| `gf2_rank(M)` | Rank of a binary matrix over GF(2) via Gaussian elimination |

## Requirements

- Python 3.x
- [NumPy](https://numpy.org/)

Install dependencies:

```bash
pip install numpy
```

## Roadmap

- [ ] TT code: implement A, B, C matrix construction and [[n, k]] output
- [ ] Code distance computation for TB and TT codes
- [ ] Support polynomial input via string parsing (e.g. `"x^3 + y"`)
- [ ] Export parity-check matrices to file
