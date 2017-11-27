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
        ('haproxy_global',),
    ]
)
def test_haproxy_single_sections(config, expected, section):
    assert list(haproxy.to_haproxy(config[section])) == expected[section]


@pytest.mark.parametrize(
    ('section',),
    [
        ('haproxy_mailers',),
        ('haproxy_peers',),
        ('haproxy_resolvers',),
        ('haproxy_userlists',),
        ('haproxy_listens',),
    ]
)
def test_haproxy_multiple_sections(config, expected, section):
    for group, options in config[section].items():
        assert list(haproxy.to_haproxy(options)) == expected[section][group]
