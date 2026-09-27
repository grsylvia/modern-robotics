"""Chapter 3: Rigid-Body Motions.

Conventions (same as the book): omega is an angular velocity 3-vector,
a twist V = [omega, v] is a 6-vector, and T is a 4x4 homogeneous transform.
"""

import numpy as np

# --- 3.2 Rotations and angular velocities ---------------------------------


def rot_inv(R):
    """Inverse of a rotation matrix R in SO(3)."""
    raise NotImplementedError


def vec_to_so3(omega):
    """3-vector -> 3x3 skew-symmetric matrix [omega]."""
    raise NotImplementedError


def so3_to_vec(so3mat):
    """3x3 skew-symmetric matrix [omega] -> 3-vector omega."""
    raise NotImplementedError


def axis_ang3(expc3):
    """Exponential coordinates omega_hat*theta -> (omega_hat, theta)."""
    raise NotImplementedError


def matrix_exp3(so3mat):
    """[omega_hat]*theta in so(3) -> R in SO(3) (Rodrigues' formula, 3.2.3)."""
    raise NotImplementedError


def matrix_log3(R):
    """R in SO(3) -> [omega_hat]*theta in so(3), theta in [0, pi] (3.2.3.3).

    Remember the special cases: R = I and trace(R) = -1.
    """
    raise NotImplementedError


# --- 3.3 Rigid-body motions and twists ------------------------------------


def rp_to_trans(R, p):
    """(R, p) -> 4x4 transform T."""
    raise NotImplementedError


def trans_to_rp(T):
    """4x4 transform T -> (R, p), with p a 3-vector."""
    raise NotImplementedError


def trans_inv(T):
    """Inverse of T, using the structure of SE(3) (don't call np.linalg.inv)."""
    raise NotImplementedError


def vec_to_se3(V):
    """Twist 6-vector [omega, v] -> 4x4 matrix [V] in se(3)."""
    raise NotImplementedError


def se3_to_vec(se3mat):
    """4x4 matrix [V] in se(3) -> twist 6-vector [omega, v]."""
    raise NotImplementedError


def adjoint(T):
    """6x6 adjoint representation [Ad_T] of T."""
    raise NotImplementedError


def screw_to_axis(q, s, h):
    """Screw axis S from a point q on the axis, unit direction s, and pitch h."""
    raise NotImplementedError


def axis_ang6(expc6):
    """Exponential coordinates S*theta -> (S, theta)."""
    raise NotImplementedError


def matrix_exp6(se3mat):
    """[S]*theta in se(3) -> T in SE(3) (3.3.3)."""
    raise NotImplementedError


def matrix_log6(T):
    """T in SE(3) -> [S]*theta in se(3) (3.3.3.2)."""
    raise NotImplementedError
