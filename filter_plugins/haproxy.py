from __future__ import unicode_literals

import collections
import sys


if sys.version_info.major < 3:
    string_types = basestring
else:
    string_types = str


# Certain options need to precede others in the configuration file. Options with
# larger weights sink to the bottom.
# Weights taken from Puppetlabs HAProxy module:
# <https://github.com/puppetlabs/puppetlabs-haproxy/blob/093b9ec1c56551a9e9679dbb3eeef87da851737e/templates/fragments/_options.erb>
OPTION_WEIGHTS = {
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


def sort_by_weight(mapping, weights=None):
    """
    Sort mapping keys first by weight, then alphabetically.
    """
    if weights:
        key = lambda kv: (weights.get(kv[0], 0), kv[0])
    else:
        key = None
    return collections.OrderedDict(sorted(mapping.items(), key=key))


def expand(options):
    """
    Expand a nested configuration dictionary.
    """
    for key, value in sort_by_weight(options, weights=OPTION_WEIGHTS).items():
        if not isinstance(value, collections.Container) or isinstance(value, string_types):
            yield (key, value)
            continue
        elif isinstance(value, collections.Sequence):
            for item in value:
                yield (key, item)
            continue
        elif isinstance(value, collections.Mapping):
            yield (key, list(expand((value))))
            continue
        yield (key, value)


def to_haproxy(options):
    """
    Yield HAProxy configuration lines from a nested configuration dictionary.
    """
    options = expand(options)
    for key, value in options:
        if value is True:
            yield str(key)
        elif value is False:
            yield 'no {}'.format(key)
        elif isinstance(value, collections.Sequence) and not isinstance(value, string_types):
            for sub_key, sub_value in value:
                yield '{} {} {}'.format(key, sub_key, sub_value)
        else:
            yield '{} {}'.format(key, value)


class FilterModule(object):
    def filters(self):
        return {
            'to_haproxy': to_haproxy,
        }
