from invoke import task

@task
def test(c):
    c.run("coverage run --source src -m py.test")

@task
def coverage(c):
    print("codecov -t")