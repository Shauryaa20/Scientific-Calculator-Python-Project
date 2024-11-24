# matrix_utils.py
import numpy as np

def matrix_add(a, b):
    if a.shape != b.shape:
        raise ValueError("Matrices must have the same dimensions for addition")
    return a + b

def matrix_subtract(a, b):
    if a.shape != b.shape:
        raise ValueError("Matrices must have the same dimensions for subtraction")
    return a - b

def matrix_multiply(a, b):
    try:
        return np.matmul(a, b)
    except ValueError:
        raise ValueError("Invalid dimensions for matrix multiplication")

def matrix_determinant(a):
    if a.shape[0] != a.shape[1]:
        raise ValueError("Matrix must be square to calculate determinant")
    return np.linalg.det(a)

def matrix_inverse(a):
    if a.shape[0] != a.shape[1]:
        raise ValueError("Matrix must be square to calculate inverse")
    return np.linalg.inv(a)

def matrix_transpose(a):
    return np.transpose(a)