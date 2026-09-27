"""Chapter 5: Velocity Kinematics and Statics.

Screw-axis lists are 6 x n arrays: column i is the screw axis of joint i.
"""

import numpy as np


def jacobian_space(s_list, theta):
    """6 x n space Jacobian J_s(theta) (5.1.1)."""
    raise NotImplementedError


def jacobian_body(b_list, theta):
    """6 x n body Jacobian J_b(theta) (5.1.2)."""
    raise NotImplementedError
