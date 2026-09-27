import modern_robotics as oracle
import numpy as np
import pytest
from helpers import (
    N_TRIALS,
    random_rotation,
    random_transform,
    random_twist,
    random_unit_vector,
)
from numpy.testing import assert_allclose

from mrlib import rigid_body as rb


@pytest.fixture
def rng():
    return np.random.default_rng(0)


# --- rotations ---------------------------------------------------------------


def test_rot_inv(rng):
    for _ in range(N_TRIALS):
        R = random_rotation(rng)
        assert_allclose(rb.rot_inv(R), oracle.RotInv(R), atol=1e-9)


def test_vec_to_so3_and_back(rng):
    for _ in range(N_TRIALS):
        w = rng.normal(size=3)
        assert_allclose(rb.vec_to_so3(w), oracle.VecToso3(w), atol=1e-9)
        assert_allclose(rb.so3_to_vec(rb.vec_to_so3(w)), w, atol=1e-9)


def test_axis_ang3(rng):
    for _ in range(N_TRIALS):
        expc3 = rng.normal(size=3)
        axis, theta = rb.axis_ang3(expc3)
        ref_axis, ref_theta = oracle.AxisAng3(expc3)
        assert_allclose(axis, ref_axis, atol=1e-9)
        assert theta == pytest.approx(ref_theta)


def test_matrix_exp3(rng):
    for _ in range(N_TRIALS):
        so3 = oracle.VecToso3(rng.normal(size=3))
        assert_allclose(rb.matrix_exp3(so3), oracle.MatrixExp3(so3), atol=1e-9)


def test_matrix_log3(rng):
    for _ in range(N_TRIALS):
        R = random_rotation(rng)
        assert_allclose(rb.matrix_log3(R), oracle.MatrixLog3(R), atol=1e-9)


def test_matrix_log3_identity():
    assert_allclose(rb.matrix_log3(np.eye(3)), np.zeros((3, 3)), atol=1e-12)


def test_matrix_log3_theta_pi(rng):
    # At theta = pi the log isn't unique, so only check that it round-trips.
    # Note: the reference library itself fails this test. Rounding puts
    # (tr R - 1)/2 just above -1, so an exact `== -1` check misses the special
    # case. Your version has to do better than the oracle here.
    for _ in range(N_TRIALS):
        R = oracle.MatrixExp3(oracle.VecToso3(np.pi * random_unit_vector(rng)))
        assert_allclose(oracle.MatrixExp3(rb.matrix_log3(R)), R, atol=1e-9)


# --- rigid-body motions ------------------------------------------------------


def test_rp_to_trans_and_back(rng):
    for _ in range(N_TRIALS):
        R, p = random_rotation(rng), rng.normal(size=3)
        T = rb.rp_to_trans(R, p)
        assert_allclose(T, oracle.RpToTrans(R, p), atol=1e-12)
        R2, p2 = rb.trans_to_rp(T)
        assert_allclose(R2, R, atol=1e-12)
        assert_allclose(p2, p, atol=1e-12)


def test_trans_inv(rng):
    for _ in range(N_TRIALS):
        T = random_transform(rng)
        assert_allclose(rb.trans_inv(T), oracle.TransInv(T), atol=1e-9)


def test_vec_to_se3_and_back(rng):
    for _ in range(N_TRIALS):
        V = random_twist(rng)
        assert_allclose(rb.vec_to_se3(V), oracle.VecTose3(V), atol=1e-12)
        assert_allclose(rb.se3_to_vec(rb.vec_to_se3(V)), V, atol=1e-12)


def test_adjoint(rng):
    for _ in range(N_TRIALS):
        T = random_transform(rng)
        assert_allclose(rb.adjoint(T), oracle.Adjoint(T), atol=1e-9)


def test_screw_to_axis(rng):
    for _ in range(N_TRIALS):
        q, s, h = rng.normal(size=3), random_unit_vector(rng), rng.normal()
        assert_allclose(rb.screw_to_axis(q, s, h), oracle.ScrewToAxis(q, s, h), atol=1e-9)


def test_axis_ang6(rng):
    for _ in range(N_TRIALS):
        expc6 = random_twist(rng)
        S, theta = rb.axis_ang6(expc6)
        ref_S, ref_theta = oracle.AxisAng6(expc6)
        assert_allclose(S, ref_S, atol=1e-9)
        assert theta == pytest.approx(ref_theta)


def test_matrix_exp6(rng):
    for _ in range(N_TRIALS):
        se3 = oracle.VecTose3(random_twist(rng))
        assert_allclose(rb.matrix_exp6(se3), oracle.MatrixExp6(se3), atol=1e-9)


def test_matrix_exp6_pure_translation(rng):
    se3 = oracle.VecTose3(np.concatenate([np.zeros(3), rng.normal(size=3)]))
    assert_allclose(rb.matrix_exp6(se3), oracle.MatrixExp6(se3), atol=1e-12)


def test_matrix_log6(rng):
    for _ in range(N_TRIALS):
        T = random_transform(rng)
        assert_allclose(rb.matrix_log6(T), oracle.MatrixLog6(T), atol=1e-9)


def test_matrix_log6_pure_translation(rng):
    T = np.eye(4)
    T[:3, 3] = rng.normal(size=3)
    assert_allclose(rb.matrix_log6(T), oracle.MatrixLog6(T), atol=1e-12)
