Role Name
========

Will install haproxy and configure it.

Requirements
------------

Only tested on CentOS, Ubuntu and SmartOS for now.
Some features are only possible with haproxy 1.5 (like the compresion flags).
This role will install the public repository to install haproxy 1.5 on ubuntu. Or it will install the EPEL repository on CentOS.

Role Variables
--------------

There is a main dictionary that needs to be set named `haproxy`.
This dictionary has 4 main sections :
- global
- defaults
- frontends
- backends

Each section has the most used parameters that I can think of. This role does not have (yet) full coverage of the main haproxy project. Feel free to submit a pull request if something is missing for you.

Example Playbook
-------------------------

I *highly* suggest that you use a seperate variable file for this role (using the `vars_files` directive), but you can use it in the main playbook if you insist:

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

See [the full example](https://github.com/Pheromone/ansible-haproxy/blob/master/vars/main.yml) to see all options.


License
-------

Apache v2

Author Information
------------------

Pheromone - Pierre Paul Lefebvre (lefebvre@pheromone.ca)
ModCloth - Rafe Colton (https://github.com/rafecolton)
