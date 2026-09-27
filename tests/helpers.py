"""Random test inputs, built without using any mrlib code."""

import numpy as np

N_TRIALS = 50


def random_unit_vector(rng):
    v = rng.normal(size=3)
    return v / np.linalg.norm(v)


def random_rotation(rng):
    q, r = np.linalg.qr(rng.normal(size=(3, 3)))
    q = q @ np.diag(np.sign(np.diag(r)))
    if np.linalg.det(q) < 0:
        q[:, 0] = -q[:, 0]
    return q


def random_transform(rng):
    T = np.eye(4)
    T[:3, :3] = random_rotation(rng)
    T[:3, 3] = rng.uniform(-2, 2, size=3)
    return T


def random_twist(rng):
    return rng.uniform(-2, 2, size=6)


def random_screw_list(rng, n):
    """6 x n list of revolute screw axes, as a random open chain would have."""
    cols = []
    for _ in range(n):
        omega = random_unit_vector(rng)
        q = rng.uniform(-1, 1, size=3)
        cols.append(np.concatenate([omega, -np.cross(omega, q)]))
    return np.array(cols).T
