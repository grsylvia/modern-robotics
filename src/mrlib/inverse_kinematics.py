"""Chapter 6: Inverse Kinematics (numerical, Newton-Raphson, 6.2).

Screw-axis lists are 6 x n arrays: column i is the screw axis of joint i.
Both functions return (theta, success).
"""

import numpy as np


def ik_body(b_list, M, T_sd, theta0, eps_omega=1e-3, eps_v=1e-3, max_iters=20):
    """Joint angles that put the end-effector at T_sd, iterating in the body frame."""
    raise NotImplementedError


def ik_space(s_list, M, T_sd, theta0, eps_omega=1e-3, eps_v=1e-3, max_iters=20):
    """Joint angles that put the end-effector at T_sd, iterating in the space frame."""
    raise NotImplementedError
