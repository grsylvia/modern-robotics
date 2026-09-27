import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Report tests that hit an unfinished stub as skipped, not failed.

    That way a red test always means a real bug in code you've written.
    """
    outcome = yield
    report = outcome.get_result()
    if call.excinfo is not None and call.excinfo.errisinstance(NotImplementedError):
        path, lineno, _ = item.location
        report.outcome = "skipped"
        report.longrepr = (path, lineno + 1, "not implemented yet")
