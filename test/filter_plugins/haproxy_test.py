import os

import pytest
import yaml

from filter_plugins import haproxy


@pytest.fixture
def config():
    config_file = os.path.join(os.path.dirname(__file__), 'fixtures', 'config.yml')
    return yaml.load(open(config_file))


@pytest.fixture
def expected():
    results_file = os.path.join(os.path.dirname(__file__), 'fixtures', 'expected.yml')
    return yaml.load(open(results_file))


@pytest.mark.parametrize(
    ('section',),
    [
        ('haproxy_defaults',),
        ('haproxy_global',)
    ]
)
def test_haproxy_defaults(config, expected, section):
    assert list(haproxy.to_haproxy(config[section])) == expected[section]
