# ansible-haproxy change log

## [Unreleased]

## [1.2.0] (2017-11-28)

### Added

* [#59] Added `tune` parameters to `global` section.
* [#69] Enabled `backports` repository for Debian Squeeze and Jessie.
* [#78] Added support for Alpine Linux.
* [#89] Added ACLs to backend.
* [#83] Added global SSL options.
* [#95] Added `reqrep` to `backend` section.
* [#98] Added `cookie` to all proxy sections.
* [#99] Added `reqadd`, `rspadd`, `reqrep`, `reqirep`, `rsprep`, `rspirep` to all proxy sections.
* [#100] Added support for `resolvers`.
* [#101] Added `maxconn` support in `listen` section.
* [#102] Added support for `force-persist`.

### Changed

* [#51] Made `haproxy.defaults.log.facility` optional.
* [#71] This role no longer elevates permissions itself. Set `become` at the playbook level.
* [#80] Use `package` module to install HAProxy.
* [#85] The default TLS configuration earns an A from SSL Labs.
* [#93] Support check mode for all install tasks.
* [#94] Validate configuration file syntax.

### Fixed

* [#68] Configuration file changes are now idempotent. This role will not restart HAProxy if no configuration files change.
* [#84] Fixed indentation for some options.
* [#94] Install HAProxy from backports repositories.
* [#96] Ignore Python bytecode.
* [#97] Fix Ubuntu detection.

### Removed

* [#54] Removed support for SmartOS.

## [1.1.0] (2017-04-11)

### Added

* [#29] Added timeout settings for `backend`, `frontend`, and `listen` sections.
* [#32] Added 503 to default list of `errorfile`s.
* [#52] Added `mode` to `listen` section.
* [#61] Enabled configuring the stats interface to listen on a dedicated address.
* [#62] Added `ssl-default-bind-ciphers` and `ssl-default-bind-options` to `global` section
* [#63] Added `reqadd` and `rspadd` to `frontend` section
* [#64] Added `errorfile` to `backend` section.
* [#69] Added `reqrep`, `reqirep`, `rsprep`, and `rspirep` to `frontend` section.
* [#70] Added `capture` to `frontend` and `http-response` to `backend` and `frontend` sections.
* [#72] Added `appsession` to `backend` and `listen`.

### Fixed

* [#34] Fixed whitespace in `frontend` template.
* [#47] Fixed bug evaluating EPEL check in check mode.
* [#48] Fixed deprecation warnings for Ansible 2.x.
* [#65] Set default values for configuration lists to avoid `with_items`/`when` conflict.
* [#66] Fixed typos in variable examples.
* [#67] Removed duplicate `http-request` in `frontend` section.
* [#73] Fixed `http-check` typos in `listen` template.

---

[1.1.0]: https://github.com/devops-coop/ansible-haproxy/compare/1.0...v1.1.0
[1.2.0]: https://github.com/devops-coop/ansible-haproxy/compare/v1.1.0...v1.2.0
[Unreleased]: https://github.com/devops-coop/ansible-haproxy/compare/v.1.20...

[#29]: https://github.com/devops-coop/ansible-haproxy/issues/29
[#32]: https://github.com/devops-coop/ansible-haproxy/issues/32
[#34]: https://github.com/devops-coop/ansible-haproxy/issues/34
[#47]: https://github.com/devops-coop/ansible-haproxy/issues/47
[#48]: https://github.com/devops-coop/ansible-haproxy/issues/48
[#51]: https://github.com/devops-coop/ansible-haproxy/issues/51
[#52]: https://github.com/devops-coop/ansible-haproxy/issues/52
[#54]: https://github.com/devops-coop/ansible-haproxy/issues/54
[#59]: https://github.com/devops-coop/ansible-haproxy/issues/59
[#61]: https://github.com/devops-coop/ansible-haproxy/issues/61
[#62]: https://github.com/devops-coop/ansible-haproxy/issues/62
[#63]: https://github.com/devops-coop/ansible-haproxy/issues/63
[#64]: https://github.com/devops-coop/ansible-haproxy/issues/64
[#65]: https://github.com/devops-coop/ansible-haproxy/issues/65
[#66]: https://github.com/devops-coop/ansible-haproxy/issues/66
[#67]: https://github.com/devops-coop/ansible-haproxy/issues/67
[#68]: https://github.com/devops-coop/ansible-haproxy/issues/68
[#69]: https://github.com/devops-coop/ansible-haproxy/issues/69
[#70]: https://github.com/devops-coop/ansible-haproxy/issues/70
[#71]: https://github.com/devops-coop/ansible-haproxy/issues/71
[#73]: https://github.com/devops-coop/ansible-haproxy/issues/73
[#78]: https://github.com/devops-coop/ansible-haproxy/issues/78
[#79]: https://github.com/devops-coop/ansible-haproxy/issues/79
[#80]: https://github.com/devops-coop/ansible-haproxy/issues/80
[#83]: https://github.com/devops-coop/ansible-haproxy/issues/83
[#84]: https://github.com/devops-coop/ansible-haproxy/issues/84
[#90]: https://github.com/devops-coop/ansible-haproxy/issues/90
[#96]: https://github.com/devops-coop/ansible-haproxy/issues/96

[#72]: https://github.com/devops-coop/ansible-haproxy/pulls/72
[#85]: https://github.com/devops-coop/ansible-haproxy/pulls/85
[#89]: https://github.com/devops-coop/ansible-haproxy/pulls/89
[#91]: https://github.com/devops-coop/ansible-haproxy/pulls/91
[#93]: https://github.com/devops-coop/ansible-haproxy/pulls/93
[#94]: https://github.com/devops-coop/ansible-haproxy/pulls/94
[#95]: https://github.com/devops-coop/ansible-haproxy/pulls/95
[#97]: https://github.com/devops-coop/ansible-haproxy/pulls/97
[#98]: https://github.com/devops-coop/ansible-haproxy/pulls/98
[#99]: https://github.com/devops-coop/ansible-haproxy/pulls/99
[#100]: https://github.com/devops-coop/ansible-haproxy/pulls/100
[#101]: https://github.com/devops-coop/ansible-haproxy/pulls/101
[#102]: https://github.com/devops-coop/ansible-haproxy/pulls/102
