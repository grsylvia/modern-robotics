"""Chapter 2: Configuration Space."""


def grubler(m, n_bodies, joint_freedoms):
    """Degrees of freedom of a mechanism by Grübler's formula (Section 2.2).

    m: 3 for planar mechanisms, 6 for spatial ones.
    n_bodies: number of links N, *including* ground.
    joint_freedoms: list of f_i, one entry per joint (so J = len(joint_freedoms)).
    """
    raise NotImplementedError
