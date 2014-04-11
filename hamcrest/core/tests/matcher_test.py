import inspect
import itertools

from hamcrest.core.string_description import StringDescription

try:
    from unittest import skipIf
    import unittest
except ImportError:
    import unittest2 as unittest

import logging

log = logging.getLogger(__name__)

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"
__tracebackhide__ = True


class MatcherTest(unittest.TestCase):

    def assert_matches(self, message, matcher, arg):
        assert_matches(matcher, arg, message)

    def assert_does_not_match(self, message, matcher, arg):
        assert_does_not_match(matcher, arg, message)

    def assert_description(self, expected, matcher):
        assert_description(expected, matcher)

    def assert_no_mismatch_description(self, matcher, arg):
        assert_no_mismatch_description(matcher, arg)

    def assert_mismatch_description(self, expected, matcher, arg):
        assert_mismatch_description(expected, matcher, arg)

    def assert_describe_mismatch(self, expected, matcher, arg):
        assert_describe_mismatch(expected, matcher, arg)


def assert_matches(matcher, arg, message):
    if inspect.isgenerator(arg):
        arg1, arg1_a, arg2, arg2_a = itertools.tee(arg, 4)
    else:
        arg1 = arg1_a = arg2 = arg2_a = arg
    try:
        assert matcher.matches(arg1), message
    except AssertionError:
        description = StringDescription()
        matcher.describe_mismatch(list(arg1_a), description)
        log.error(str(description))
        raise
    assert matcher.eq == arg2, "The equality proxy had a mismatch; {0} != {1}".format(
        matcher.eq, list(arg2_a))
    

def assert_does_not_match(matcher, arg, message):
    if inspect.isgenerator(arg):
        arg1, arg2 = itertools.tee(arg, 2)
    else:
        arg1 = arg2 = arg
    assert not matcher.matches(arg1), message
    assert matcher.eq != arg2, "The equality proxy matched unexpectedly"


def assert_description(expected, matcher):
    description = StringDescription()
    description.append_description_of(matcher)
    assert expected == str(description)


def assert_no_mismatch_description(matcher, arg):
    description = StringDescription()
    result = matcher.matches(arg, description)
    assert result, 'Precondition: Matcher should match item'
    assert '' == str(description), 'Expected no mismatch description'


def assert_mismatch_description(expected, matcher, arg):
    description = StringDescription()
    result = matcher.matches(arg, description)
    assert not result, 'Precondition: Matcher should not match item'
    assert expected == str(description)


def assert_describe_mismatch(expected, matcher, arg):
    description = StringDescription()
    matcher.describe_mismatch(arg, description)
    assert expected == str(description)
