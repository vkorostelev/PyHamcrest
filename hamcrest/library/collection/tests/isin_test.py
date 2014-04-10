from __future__ import absolute_import

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"

from hamcrest.core.string_description import tostring
from hamcrest.library.collection.isin import is_in

import pytest


@pytest.fixture(params=[list, iter])
def sequence(request):
    return request.param(('a', 'b', 'c'))

    
@pytest.fixture
def matcher(sequence):
    return is_in(sequence)


@pytest.fixture(params=('a', 'b', 'c'))
def valid_value(request):
    return request.param


@pytest.fixture
def description(matcher):
    return "one of ('{0}')".format("', '".join(matcher.sequence))


@pytest.fixture
def mismatch_description(invalid_value):
    return "was {0}".format(tostring(invalid_value))
    

@pytest.fixture(params=(1, object()))
def invalid_value(request):
    return request.param

    
from hamcrest.core.tests.generic_matcher_test import *
