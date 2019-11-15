"""Nox file which runs tests and linting."""
import nox


@nox.session
def tests(session):
    """Running tests."""
    session.install("pipenv")
    session.run("pipenv", "sync", "--dev")
    session.run(
        "pipenv", "run", "pytest", "--disable-warnings",
    )


@nox.session
def lint(session):
    """Linting using black/flake8."""
    session.install("wemake-python-styleguide", "black", "isort")
    session.run("isort", "-rc", ".")
    session.run("black", "--line-length", "99", "--check", ".")
    session.run("flake8", "g_packer")
