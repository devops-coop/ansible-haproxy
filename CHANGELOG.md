# ansible-haproxy change log

## 2.x (unreleased)

### Added

* [#78] Added support for Alpine Linux. Thanks, **[\@roedie]**!
* [#89] Added ACLs to backend. Thanks, **[\@aarnaud]**!

### Changed

* [#71] This role no longer elevates permissions itself. Set `become` at the playbook level.
* [#85] The default TLS configuration earns an A from SSL Labs. Thanks, **[\@reminec]**!

### Fixed

* [#68] Configuration file changes are now idempotent. This role will not restart HAProxy if no configuration files change. Thanks, **[\@aarnaud]**!

### Removed

* [#54] Removed support for SmartOS.

## 1.1.0 (2017-04-11)

### Added

* [#29] Added timeout settings for `backend`, `frontend`, and `listen` sections.
* [#32] Added 503 to default list of `errorfile`s. Thanks, **[\@nathanielks]**!
* [#52] Added `mode` to `listen` section. Thanks, **[\@dekhtyarev]**!
* [#59] Added `tune` parameters to `global` section.
* [#61] Enabled configuring the stats interface to listen on a dedicated address. Thanks, **[\@fw8]**!
* [#62] Added `ssl-default-bind-ciphers` and `ssl-default-bind-options` to `global` section Thanks, **[\@fw8]**!
* [#63] Added `reqadd` and `rspadd` to `frontend` section Thanks, **[\@fw8]**!
* [#64] Added `errorfile` to `backend` section. Thanks, **[\@fw8]**!
* [#69] Added `reqrep`, `reqirep`, `rsprep`, and `rspirep` to `frontend` section. Thanks, **[\@hany]**!
* [#69] Enabled `backports` repository for Debian Squeeze and Jessie.
* [#70] Added `capture` to `frontend` and `http-response` to `backend` and `frontend` sections. Thanks, **[\@hany]**!
* [#72] Added `appsession` to `backend` and `listen`. Thanks, **[\@fw8]**!

### Changed

* [#51] Made `haproxy.defaults.log.facility` optional.

### Fixed

* [#34] Fixed whitespace in `frontend` template. Thanks, **[\@noirbee]**!
* [#47] Fixed bug evaluating EPEL check in check mode.
* [#48] Fixed deprecation warnings for Ansible 2.x. Thanks, **[\@UnderGreen]**!
* [#65] Set default values for configuration lists to avoid `with_items`/`when` conflict.
* [#66] Fixed typos in variable examples. Thanks, **[\@clwells]**!
* [#67] Removed duplicate `http-request` in `frontend` section. Thanks, **[\@clwells]**!
* [#73] Fixed `http-check` typos in `listen` template.

---

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
[#72]: https://github.com/devops-coop/ansible-haproxy/issues/72
[#73]: https://github.com/devops-coop/ansible-haproxy/issues/73
[#78]: https://github.com/devops-coop/ansible-haproxy/issues/78
[#85]: https://github.com/devops-coop/ansible-haproxy/issues/85
[#89]: https://github.com/devops-coop/ansible-haproxy/issues/89
[\@UnderGreen]: https://github.com/UnderGreen
[\@aarnaud]: https://github.com/aarnaud
[\@clwells]: https://github.com/clwells
[\@dekhtyarev]: https://github.com/dekhtyarev
[\@fw8]: https://github.com/fw8
[\@hany]: https://github.com/hany
[\@nathanielks]: https://github.com/nathanielks
[\@noirbee]: https://github.com/noirbee
[\@onitake]: https://github.com/onitake
[\@reminec]: https://github.com/reminec
[\@roedie]: https://github.com/roedie
