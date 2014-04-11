from __future__ import absolute_import
from .selfdescribing import SelfDescribing
from .string_description import tostring

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class Matcher(SelfDescribing):
    """A matcher over acceptable values.

    A matcher is able to describe itself to give feedback when it fails.

    Matcher implementations should *not* directly implement this protocol.
    Instead, *extend* the :py:class:`~hamcrest.core.base_matcher.BaseMatcher`
    class, which will ensure that the
    :py:class:`~hamcrest.core.matcher.Matcher` API can grow to support new
    features and remain compatible with all
    :py:class:`~hamcrest.core.matcher.Matcher` implementations.

    """

    def matches(self, item, mismatch_description=None):
        """Evaluates the matcher for argument item.

        If a mismatch is detected and argument ``mismatch_description`` is
        provided, it will generate a description of why the matcher has not
        accepted the item.

        :param item: The object against which the matcher is evaluated.
        :returns: ``True`` if ``item`` matches, otherwise ``False``.

        """
        raise NotImplementedError('matches')

    def describe_mismatch(self, item, mismatch_description):
        """Generates a description of why the matcher has not accepted the
        item.

        The description will be part of a larger description of why a matching
        failed, so it should be concise.

        This method assumes that ``matches(item)`` is ``False``, but will not
        check this.

        :param item: The item that the
            :py:class:`~hamcrest.core.matcher.Matcher` has rejected.
        :param mismatch_description: The description to be built or appended
            to.

        """
        raise NotImplementedError('describe_mismatch')

    @property
    def eq(self):
        """Return a proxy for this matcher that implements equality checking for
        objects
        
        >>> class MatcherClass(Matcher):
        ...    def matches(self, obj, *a):
        ...        return obj == '1'
        
        >>> m = MatcherClass()
        >>> m.matches('1')
        True
        >>> m.eq == '1'
        True
        >>> m.matches(1)
        False
        >>> m.eq == 1
        False
        >>> m.eq != 1
        True

        """
        class Proxy(self.__class__):
            def __init__(ps):
                ps.matcher = self
                
            def __eq__(ps, object):
                return ps.matcher.matches(object)

            def __ne__(ps, object):
                return not ps.matcher.matches(object)

            def __str__(ps):
                return repr(ps.matcher)

            def __repr__(ps):
                return tostring(ps.matcher)
        Proxy.__name__ = '{0}Equality'.format(self.__class__.__name__)
        proxy = Proxy()
        return proxy
