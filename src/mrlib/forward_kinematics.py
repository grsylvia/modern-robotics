"""Chapter 4: Forward Kinematics (product of exponentials).

Screw-axis lists are 6 x n arrays: column i is the screw axis of joint i.
"""

import numpy as np


def fk_space(M, s_list, theta):
    """End-effector pose from space-frame screw axes (4.1.1).

    T = e^[S1]th1 ... e^[Sn]thn M
    """
    raise NotImplementedError


def fk_body(M, b_list, theta):
    """End-effector pose from body-frame screw axes (4.1.3).

    T = M e^[B1]th1 ... e^[Bn]thn
    """
    raise NotImplementedError
