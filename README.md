# modern-robotics

Working through *Modern Robotics: Mechanics, Planning, and Control* (Lynch & Park)
and implementing the math from scratch as `mrlib`, one chapter at a time.

- Book (free preprint) and videos: http://hades.mech.northwestern.edu/index.php/Modern_Robotics
- Reference library: [`modern_robotics`](https://github.com/NxRLab/ModernRobotics), used **only** as a test oracle

## Setup

```bash
python3 -m venv .venv
.venv/bin/pip install -e '.[dev]'
.venv/bin/pytest
```

Tests compare `mrlib` with the reference library on random inputs. An unfinished
stub (`raise NotImplementedError`) shows up as **skipped**, so a failure always
means a real bug in code you've written.

## Workflow per chapter

1. Read the chapter and watch its videos.
2. Do a few end-of-chapter exercises on paper.
3. Implement the stubs in `src/mrlib/` without looking at the reference library's source.
4. Keep going until the chapter's tests pass, then move on.

## Progress

| Ch | Topic | Module | Status |
|----|-------|--------|--------|
| 2 | Configuration space | `configuration_space.py` | ☐ |
| 3 | Rigid-body motions | `rigid_body.py` | ☐ |
| 4 | Forward kinematics | `forward_kinematics.py` | ☐ |
| 5 | Velocity kinematics | `velocity_kinematics.py` | ☐ |
| 6 | Inverse kinematics | `inverse_kinematics.py` | ☐ |
| 8 | Dynamics of open chains | — | later |
| 9 | Trajectory generation | — | later |
| 11 | Robot control | — | later |

## Conventions

Same as the book: twists are `[omega, v]`, and screw-axis lists are `6 x n` arrays
with one column per joint.
