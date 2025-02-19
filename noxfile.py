import nox


@nox.session(python="3.9", reuse_venv=True)
def dev(session):
    """For creating a development virtual environment. Handy for setting interpreter in
    IDE.
    """
    session.install("-r", "test-requirements.txt")


@nox.session(python="3.9", reuse_venv=True)
def format(session):
    session.install("black")
    session.run("black", "business_rules", "test", *session.posargs)


@nox.session(python="3.9", reuse_venv=True)
def lint(session):
    session.install("flake8")
    session.run("flake8", "business_rules", "test")


@nox.session(python=["3.7", "3.8", "3.9"], reuse_venv=True)
def test(session):
    session.install("-r", "test-requirements.txt")

    session.run("pytest", *session.posargs)
