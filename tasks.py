from invoke import task


@task(aliases=["u"])
def update(c):
    print("Updating dependencies...")
    c.run("pip install --upgrade pip")


@task(aliases=["c"])
def clean(c):
    print("Cleaning up...")
    c.run("rm -rf coverage")
    c.run("rm -rf dist")
    c.run("rm -f .coverage")
    c.run("rm -f coverage.xml")
    c.run("rm -rf htmlcov")
    c.run("rm -rf tests/htmlcov")
    c.run("rm -rf tests/.pytest_cache")
    c.run("rm -rf ./.pytest_cache")
    c.run("rm -f tests/coverage.xml")


@task(aliases=["t"])
def test(c):
    """Runs PyTest unit tests."""
    c.run("pytest tests")


@task(aliases=["v"])
def cover(c):
    """Runs PyTest unit and integration tests with coverage."""
    c.run("coverage run -m pytest")
    c.run("coverage lcov -o ./coverage/lcov.info")


@task(aliases=["l"])
def lint(c):
    print("Linting...")
    c.run(
        "poetry run flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics"
    )
    c.run(
        "poetry run flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics"
    )


@task(aliases=["b"], pre=[clean, lint, cover], default=True)
def build(c):
    print("Building the project")
    c.run("poetry build")
