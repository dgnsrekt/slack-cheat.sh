"""Nox file which runs tests and linting."""
import nox


@nox.session()
def tests(session):
    """Running tests."""
    session.install("pipenv")
    session.run("pipenv", "install", "--dev")
    session.run(
        "pipenv", "run", "pytest", "--quiet",
    )


@nox.session
def lint(session):
    """Linting using black/flake8."""
    session.install("wemake-python-styleguide", "black", "isort")
    session.run("isort", "-rc", "tests")
    session.run("isort", "-rc", "slack_cheat")
    session.run("black", "--line-length", "99", "--check", "slack_cheat", "tests")
    session.run("flake8", "slack_cheat")
