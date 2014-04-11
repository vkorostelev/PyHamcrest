def pytest_ignore_collect(path, config):
    return str(path).endswith('generic_matcher_test.py')


