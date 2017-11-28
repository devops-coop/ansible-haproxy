haproxy
=======

Installs and configures [HAProxy 1.5](http://www.haproxy.org/).

Versions
--------

**WARNING:** This is the README for the `master` branch, which tracks the development of version 2 and targets Ansible 2.x. This branch is under active development and will include breaking changes.

The **last release** in the 1.x series is [1.2.0](https://github.com/devops-coop/ansible-haproxy/tree/v1.2.0).

Features
--------

* Offers flexible, structured configuration syntax.
* Supports Alpine, CentOS, Debian, and Ubuntu.
* Installs HAProxy 1.5 from official repositories on Debian and Ubuntu.
* Installs EPEL repository on CentOS.

Role Variables
--------------

* `haproxy_global`

    Global HAProxy settings.
* `haproxy_defaults`

    Default settings for frontends, backends, and listen proxies.
* `haproxy_mailers`

    A map of [`mailers` configurations](https://cbonte.github.io/haproxy-dconv/1.8/configuration.html#3.6) sections.
* `haproxy_peers`

    A map of [`peer` configurations](https://cbonte.github.io/haproxy-dconv/1.8/configuration.html#3.5).
* `haproxy_resolvers`

    A map of [`resolvers` configurations](https://cbonte.github.io/haproxy-dconv/1.8/configuration.html#5.3.2).
* `haproxy_userlists`

    A map of [`userlist` configurations](https://cbonte.github.io/haproxy-dconv/1.8/configuration.html#3.4).
* `haproxy_backends`

    A map of [`backend` configurations](https://cbonte.github.io/haproxy-dconv/1.8/configuration.html#4).
* `haproxy_frontends`

    A map of [`frontend` configurations](https://cbonte.github.io/haproxy-dconv/1.8/configuration.html#4).
* `haproxy_listen`

    A map of [`listen` configurations](https://cbonte.github.io/haproxy-dconv/1.8/configuration.html#4).

Configuration
-------------

HAProxy is a complex piece of software and supports hundreds of configuration options.

Rather than support individual options, this role offers a flexible, structured configuration syntax for HAProxy concepts.

For example, instead of declaring `errorfile` lines like this:

```yaml
haproxy_defaults:
  errorfile:
    - code: 400
      file: /etc/haproxy/errors/400.http
    - code: 403
      file: /etc/haproxy/errors/403.http
```

You would use the following natural syntax:

```yaml
haproxy_defaults:
  errorfile:
    400: /etc/haproxy/errors/400.http
    403: /etc/haproxy/errors/403.http
```

The descriptions below detail how the role handles different data types.

### Maps

The template expands maps (dictionaries, hashes) according to three simple rules:

1. Prefix every value in the map with the key name.
2. Sort option names by relative weight. This ensures HAProxy processes `acl` rules before `http-request` rules, for example.
3. Within each weighted group, sort option names alphabetically.

This ensures predictable output and eliminates runtime warnings.

```yaml
---
haproxy_defaults:
  timeout:
    server: 500ms
    connect: 1000s
    client: 5000s
  retries: 5
  option:
    - forwardfor
    - dontlognull
```

```
defaults
    option forwardfor
    option dontlognull
    retries 5
    timeout client 5000s
    timeout connect 1000s
    timeout server 500ms
```

### Sequences

The template will preserve sequence (list, array) order. This is important in some contexts, such as `http-request` rules.

```yaml
---
haproxy_frontends:
  http-in:
    acl:
      - is_admin path_beg /admin
      - is_api   path_beg /api
    default_backend: http
```

```
frontend http-in
    acl is_admin path_beg /admin
    acl is_api   path_beg /api
    default_backend http
```

### Booleans

True values (`true`, `yes`, `y`, etc.) will expand to simple flags:

```yaml
---
haproxy_backends:
  http:
    disabled: true
    server:
      www: 192.0.2.1:80
```

```
backend http
  disabled
  server www 192.0.2.1:80
```

False values will omit the flag:

```yaml
---
haproxy_backends:
  http:
    disabled: false
    server:
      www: 192.0.2.1:80
```

```
backend http
  server www 192.0.2.1:80
```

### Strings, integers, floats, and other primitives

Other primitives will be rendered as-is:

```yaml
haproxy_listens:
  tcp-in:
    backlog: 10000
    maxconn: 1000
    mode: tcp
```

```
listen tcp-in
    backlog 10000
    maxconn 1000
    mode tcp
```

Example
-------

```yaml
---
haproxy_frontends:
  http:
    bind:
      - :80
      - :443 ssl crt /etc/ssl/certs/star.example.org.pem
    acl:
      - is_api hdr(Host) api.example.org
    use_backend:
      - api if is_api
    redirect:
      - scheme https if { !ssl_fc }
    default_backend: app

haproxy_backends:
  app:
    server:
      app-01: 192.51.100.10:80 check
      app-02: 192.51.100.11:80 check

  api:
    server:
      api-01: 192.51.100.100:80 check
      api-02: 192.51.100.101:80 check
```

License
-------

Apache v2
