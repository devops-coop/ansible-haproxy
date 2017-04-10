haproxy
========

Installs and configures [HAProxy 1.5](http://www.haproxy.org/).

Features
--------

* Supports CentOS, Debian, Ubuntu, and SmartOS.
* Installs HAProxy 1.5 from official repositories on Debian, Ubuntu, and SmartOS.
* Installs EPEL repository on CentOS.

Role Variables
--------------

* `haproxy_global`

    Global HAProxy settings.
* `haproxy_defaults`

    Default settings for frontends, backends, and listen proxies.
* `haproxy_backends`

    A list of HAProxy backends.
* `haproxy_frontends`

    A list of HAProxy frontends.
* `haproxy_listen`

    A list of listen proxies.

See [`vars/main.yml`](vars/main.yml) for a complete list of configurable .

Example
-------

```yaml
- hosts: loadbalancers
  roles:
     - role: haproxy
       haproxy_frontends:
       - name: 'fe-mysupersite'
         ip: '123.123.123.120'
         port: '80'
         maxconn: '1000'
         default_backend: 'be-mysupersite'
       haproxy_backends:
       - name: 'be-mysupersite'
         description: 'mysupersite is really cool'
         servers:
           - name: 'be-mysupersite-01'
             ip: '192.168.1.100'
```

License
-------

Apache v2
