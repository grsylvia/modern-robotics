from mrlib import configuration_space as cs


def test_four_bar_linkage():
    # planar, 4 links incl. ground, 4 revolute joints -> 1 dof
    assert cs.grubler(3, 4, [1, 1, 1, 1]) == 1


def test_stewart_platform():
    # spatial, 14 links incl. ground, 6 universal + 6 prismatic + 6 spherical -> 6 dof
    assert cs.grubler(6, 14, [2] * 6 + [1] * 6 + [3] * 6) == 6


def test_open_chain_6r_arm():
    # spatial, 7 links incl. ground, 6 revolute joints -> 6 dof
    assert cs.grubler(6, 7, [1] * 6) == 6
