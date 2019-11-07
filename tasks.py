from invoke import task

@task
def test(c):
    c.run("coverage run --source src -m py.test")

@task
def coverage(c):
    c.run("codecov -t")