import modern_robotics as oracle
import numpy as np
import pytest
from helpers import N_TRIALS, random_screw_list, random_transform
from numpy.testing import assert_allclose

from mrlib import forward_kinematics as fk
from mrlib import inverse_kinematics as ik
from mrlib import velocity_kinematics as vk

N_JOINTS = 6


@pytest.fixture
def rng():
    return np.random.default_rng(0)


def random_chain(rng):
    """(M, s_list, b_list) for a random 6R open chain."""
    M = random_transform(rng)
    s_list = random_screw_list(rng, N_JOINTS)
    b_list = oracle.Adjoint(oracle.TransInv(M)) @ s_list
    return M, s_list, b_list


def random_joints(rng):
    return rng.uniform(-np.pi, np.pi, size=N_JOINTS)


# --- Chapter 4 ---------------------------------------------------------------


def test_fk_space(rng):
    for _ in range(N_TRIALS):
        M, s_list, _ = random_chain(rng)
        th = random_joints(rng)
        assert_allclose(fk.fk_space(M, s_list, th), oracle.FKinSpace(M, s_list, th), atol=1e-9)


def test_fk_body(rng):
    for _ in range(N_TRIALS):
        M, _, b_list = random_chain(rng)
        th = random_joints(rng)
        assert_allclose(fk.fk_body(M, b_list, th), oracle.FKinBody(M, b_list, th), atol=1e-9)


def test_fk_zero_config_is_home(rng):
    M, s_list, b_list = random_chain(rng)
    zeros = np.zeros(N_JOINTS)
    assert_allclose(fk.fk_space(M, s_list, zeros), M, atol=1e-12)
    assert_allclose(fk.fk_body(M, b_list, zeros), M, atol=1e-12)


# --- Chapter 5 ---------------------------------------------------------------


def test_jacobian_space(rng):
    for _ in range(N_TRIALS):
        _, s_list, _ = random_chain(rng)
        th = random_joints(rng)
        assert_allclose(vk.jacobian_space(s_list, th), oracle.JacobianSpace(s_list, th), atol=1e-9)


def test_jacobian_body(rng):
    for _ in range(N_TRIALS):
        _, _, b_list = random_chain(rng)
        th = random_joints(rng)
        assert_allclose(vk.jacobian_body(b_list, th), oracle.JacobianBody(b_list, th), atol=1e-9)


# --- Chapter 6 ---------------------------------------------------------------
# IK solutions aren't unique, so check that the answer reaches the target
# rather than comparing joint angles.


def ik_problems(rng):
    for _ in range(N_TRIALS):
        M, s_list, b_list = random_chain(rng)
        th_true = random_joints(rng)
        T_sd = oracle.FKinSpace(M, s_list, th_true)
        theta0 = th_true + rng.uniform(-0.1, 0.1, size=N_JOINTS)
        yield M, s_list, b_list, T_sd, theta0


def test_ik_body(rng):
    for M, _, b_list, T_sd, theta0 in ik_problems(rng):
        th, success = ik.ik_body(b_list, M, T_sd, theta0, 1e-6, 1e-6)
        assert success
        assert_allclose(oracle.FKinBody(M, b_list, th), T_sd, atol=1e-5)


def test_ik_space(rng):
    for M, s_list, _, T_sd, theta0 in ik_problems(rng):
        th, success = ik.ik_space(s_list, M, T_sd, theta0, 1e-6, 1e-6)
        assert success
        assert_allclose(oracle.FKinSpace(M, s_list, th), T_sd, atol=1e-5)
