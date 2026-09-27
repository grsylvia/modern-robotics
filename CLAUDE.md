# CLAUDE.md

This is a learning repo. The user is working through *Modern Robotics* and
writes the math in `src/mrlib/` themselves.

- **Don't implement the functions in `src/mrlib/`** unless the user explicitly
  asks for the solution. Explain concepts, point to the book section, give hints,
  and review the user's code instead.
- You may write or extend tests, plotting and visualization helpers, and tooling.
- Tests use the `modern_robotics` package as an oracle. Its `MatrixLog3` is
  numerically fragile near theta = pi, and `test_matrix_log3_theta_pi` checks for
  exactly that, so don't "fix" the test to match the oracle.
- Run tests with `.venv/bin/pytest`. The ROS 2 pytest plugins are disabled in
  `pyproject.toml` because the user's shell sources ROS.
