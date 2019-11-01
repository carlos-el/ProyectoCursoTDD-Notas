from invoke import task

@task
def test(c):
    c.run("py.test")

@task
def build(c):
    print("Building")