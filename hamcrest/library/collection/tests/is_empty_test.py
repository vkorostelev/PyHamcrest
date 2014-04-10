from __future__ import absolute_import

from hamcrest.library.collection.is_empty import empty

from hamcrest.core.tests.matcher_test import MatcherTest
import pytest

__author__ = "Chris Rose"
__copyright__ = "Copyright 2012 hamcrest.org"
__license__ = "BSD, see License.txt"

class LengthHaver(object):

    def __init__(self, len_):
        self._len = len_

    def __len__(self):
        return self._len

class EmptyCollectionTest(MatcherTest):

    def testReturnsTrueForEmptyStandardCollections(self):
        matcher = empty()
        self.assert_matches('empty tuple', matcher, ())
        self.assert_matches('empty list', matcher, [])
        self.assert_matches('emtpy dictionary', matcher, {})

    def testReturnsTrueForEmptyCollectionLike(self):
        matcher = empty()
        self.assert_matches('empty protocol object', matcher, LengthHaver(0))

    def testReturnsFalseForNonEmptyStandardCollections(self):
        matcher = empty()
        self.assert_does_not_match('non-empty tuple', matcher, (1,))
        self.assert_does_not_match('non-empty list', matcher, [1])
        self.assert_does_not_match('emtpy dictionary', matcher, {1:2})

    def testReturnsFalseForNonEmptyCollectionLike(self):
        matcher = empty()
        self.assert_does_not_match('non-empty protocol object', matcher, LengthHaver(1))

    def testHasReadableDescription(self):
        self.assert_description("an empty collection", empty())

    def testSuccessfulMatchDoesNotGenerateMismatchDescription(self):
        self.assert_no_mismatch_description(empty(), [])

    def testDescribeMismatch(self):
        self.assert_mismatch_description("has 3 item(s)", empty(), [1,2,3])
        self.assert_mismatch_description("does not support length", empty(), 1)


@pytest.fixture
def matcher():
    return empty()


@pytest.fixture(params=((), [], {}, LengthHaver(0)))
def valid_value(request):
    return request.param


@pytest.fixture(params=((1,), [1], {1: 2}, LengthHaver(1), 1))
def invalid_value(request):
    return request.param


@pytest.fixture
def description():
    return "an empty collection"


@pytest.fixture
def mismatch_description(invalid_value):
    if invalid_value == 1:
        return 'does not support length'
    return 'has {0} item(s)'.format(len(invalid_value))


from hamcrest.core.tests.generic_matcher_test import *

