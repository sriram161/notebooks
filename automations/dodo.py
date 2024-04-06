def task_unitest():
    c1 = "coverage erase"
    c2 = "coverage run -m pytest -v"
    c3 = "coverage report -m"
    c4 = "coverage xml"
    return dict(actions=[c1 ,c2, c3, c4], doc="doit unitest", task_dep=[])

def task_build():
    c1 = ["docker-compose build --no-cache %(service)s"]
    task = dict(actions=[c1], task_dep=[], verbosity=2, params=[{"name": "service", "s", "default": ""}],)
    return task

if __name__ == "__main__":
    import doit
    doit.run(globals())