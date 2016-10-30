# -*- coding: utf-8 -*-

def flatten(d, separator='.'):
    """
    Flatten a dictionary `d` by joining nested keys with `separator`.

    Slightly modified from <http://codereview.stackexchange.com/a/21035>.

    >>> flatten({'eggs': 'spam', 'sausage': {'eggs': 'bacon'}, 'spam': {'bacon': {'sausage': 'spam'}}})
    {'spam.bacon.sausage': 'spam', 'eggs': 'spam', 'sausage.eggs': 'bacon'}
    """
    def items():
        for k, v in d.items():
            try:
                for sub_k, sub_v in flatten(v, separator).items():
                    yield separator.join([k, sub_k]), sub_v
            except AttributeError:
                yield k, v
    return dict(items())


class FilterModule(object):
    def filters(self):
        return {'flatten': flatten}
