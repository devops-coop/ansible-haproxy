from __future__ import unicode_literals

import collections
import sys


if sys.version_info.major < 3:
    string_types = basestring
else:
    string_types = str


# Ranks taken from Puppetlabs HAProxy module:
# <https://github.com/puppetlabs/puppetlabs-haproxy/blob/093b9ec1c56551a9e9679dbb3eeef87da851737e/templates/fragments/_options.erb>
RANKS = {
    'acl': -1,
    'tcp-request': 2,
    'block': 3,
    'http-request': 4,
    'reqallow': 5,
    'reqdel': 5,
    'reqdeny': 5,
    'reqidel': 5,
    'reqideny': 5,
    'reqipass': 5,
    'reqirep': 5,
    'reqitarpit': 5,
    'reqpass': 5,
    'reqrep': 5,
    'reqtarpit': 5,
    'reqadd': 6,
    'redirect': 7,
    'use_backend': 8,
    'use-server': 9,
    'server': 100,
}


def haproxy_sort(options):
    """
    Sort HAProxy options according to their relative ranks.
    """
    return collections.OrderedDict(
        sorted(options.items(), key=lambda pair: RANKS.get(pair[0], 0)),
    )


def flatten(iterable):
    """
    Flatten nested iterables to a single level.
    """
    for item in iterable:
        if isinstance(item, collections.Iterable) and not isinstance(item, string_types):
            for subitem in flatten(item):
                yield subitem
        else:
            yield item


def expand(options):
    """
    Expand a nested configuration dictionary.
    """
    for key, value in options.items():
        if isinstance(value, collections.Mapping):
            yield (key, value.items())
        elif isinstance(value, string_types):
            yield (key, value)
        elif isinstance(value, collections.Iterable):
            for item in value:
                yield (key, item)
        elif value is True:
            yield (key, None)
        else:
            yield (key, value)


def to_haproxy(options):
    """
    Yield HAProxy configuration lines from a nested configuration dictionary.
    """
    options = haproxy_sort(options)
    for key, value in expand(options):
        if value is None:
            yield key
            continue
        if not isinstance(value, collections.Iterable) or isinstance(value, string_types):
            value = [value]
        yield '{} {}'.format(key, ' '.join(str(v) for v in flatten(value)))


class FilterModule(object):
    def filters(self):
        return {
            'to_haproxy': to_haproxy,
        }
