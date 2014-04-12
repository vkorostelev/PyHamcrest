def pytest_ignore_collect(path, config):
    if path.basename == 'setup.py':
        return True

    if path.dirpath().basename == 'examples':
        return True

    if path.dirpath().basename == 'doc':
        return True
