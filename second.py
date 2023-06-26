import numpy as np


def is_M_matrix(m):
    rows, cols = m.shape

    if (m[~np.eye(rows, dtype=bool)] > 0).any():
        return False

    eigenvalues = np.linalg.eigvals(m)

    if np.any(np.real(eigenvalues) < 0):
        return False

    return True


# Пример 1
m1 = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
print(is_M_matrix(m1))  # True

# Пример 2
m2 = np.array([[1, 2, 0], [0, 2, 0], [0, 0, 3]])
print(is_M_matrix(m2))  # False

# Пример 3
m3 = np.array([[1, -2, 0], [0, 2, 0], [0, 0, 3]])
print(is_M_matrix(m3))  # False
