# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-container/#history

## [2.0.0](https://www.github.com/googleapis/python-container/compare/v1.0.1...v2.0.0) (2020-07-16)


### ⚠ BREAKING CHANGES

* migrate to microgenerator (#33)

### Features

* migrate to microgenerator ([#33](https://www.github.com/googleapis/python-container/issues/33)) ([aa9b20c](https://www.github.com/googleapis/python-container/commit/aa9b20c6f4ccb6dff305bfcd72e1bde4a1ee86cd))

### [1.0.1](https://www.github.com/googleapis/python-container/compare/v1.0.0...v1.0.1) (2020-06-16)


### Bug Fixes

* fix `release_status` in `setup.py` ([#27](https://www.github.com/googleapis/python-container/issues/27)) ([d853d99](https://www.github.com/googleapis/python-container/commit/d853d99c73f4716721aa26d96ec6bc1a5c916dc4))

## [1.0.0](https://www.github.com/googleapis/python-container/compare/v0.5.0...v1.0.0) (2020-06-16)


### Features

* release as production/stable ([#24](https://www.github.com/googleapis/python-container/issues/24)) ([0e0095d](https://www.github.com/googleapis/python-container/commit/0e0095d8fad004d8098af62c6c27a40aa96d6257))

## [0.5.0](https://www.github.com/googleapis/python-container/compare/v0.4.0...v0.5.0) (2020-04-14)


### Features

* make `project_id`, `zone`, `cluster_id`, `node_pool` optional arguments to methods in `cluster_manager_client`; change default timeout config; add 2.7 sunset warning; bump copyright year to 2020 (via synth)([#8](https://www.github.com/googleapis/python-container/issues/8)) ([6afc050](https://www.github.com/googleapis/python-container/commit/6afc050f21c57a2d0eda3327c07510f2226aa6a6))

## [0.4.0](https://www.github.com/googleapis/python-container/compare/v0.3.0...v0.4.0) (2020-02-03)


### Features

* **container:** add 'list_usable_subnetworks' method; apply proto annotations (via synth) ([#9741](https://www.github.com/googleapis/python-container/issues/9741)) ([541a9e3](https://www.github.com/googleapis/python-container/commit/541a9e3974c38e2601c17c569099ce8602a1c4be))

## 0.3.0

07-30-2019 10:28 PDT


### Implementation Changes

### New Features
- Add 'client_options' support, update list method docstrings (via synth). ([#8501](https://github.com/googleapis/google-cloud-python/pull/8501))
- Add synth support for v1beta1 API version (via manual synth). ([#8436](https://github.com/googleapis/google-cloud-python/pull/8436))
-  Allow kwargs to be passed to create_channel (via synth).  ([#8384](https://github.com/googleapis/google-cloud-python/pull/8384))

### Dependencies
- Bump minimum version for google-api-core to 1.14.0. ([#8709](https://github.com/googleapis/google-cloud-python/pull/8709))
- Update pin for 'grpc-google-iam-v1' to 0.12.3+. ([#8647](https://github.com/googleapis/google-cloud-python/pull/8647))
- Remove classifier for Python 3.4 for end-of-life. ([#7535](https://github.com/googleapis/google-cloud-python/pull/7535))

### Documentation
- Update intersphinx mapping for requests. ([#8805](https://github.com/googleapis/google-cloud-python/pull/8805))
- Link to googleapis.dev documentation in READMEs. ([#8705](https://github.com/googleapis/google-cloud-python/pull/8705))
- Add compatibility check badges to READMEs. ([#8288](https://github.com/googleapis/google-cloud-python/pull/8288))
- Add docs job to publish to googleapis.dev. ([#8464](https://github.com/googleapis/google-cloud-python/pull/8464))

### Internal / Testing Changes
- Pin black version (via synth). ([#8575](https://github.com/googleapis/google-cloud-python/pull/8575))
- Declare encoding as utf-8 in pb2 files (via synth). ([#8347](https://github.com/googleapis/google-cloud-python/pull/8347))
- Add disclaimer to auto-generated template files (via synth).  ([#8309](https://github.com/googleapis/google-cloud-python/pull/8309))
- Update noxfile and setup.py (via synth). ([#8298](https://github.com/googleapis/google-cloud-python/pull/8298))
- Blacken (via synth). ([#8285](https://github.com/googleapis/google-cloud-python/pull/8285))
- Add routing header to method metadata, add nox session `docs` (via synth). ([#7922](https://github.com/googleapis/google-cloud-python/pull/7922))
- Copy proto files alongside protoc versions.
- Minor gapic-generator change. ([#7225](https://github.com/googleapis/google-cloud-python/pull/7225))
- Add protos as an artifact to library ([#7205](https://github.com/googleapis/google-cloud-python/pull/7205))
- Update copyright headers ([#7140](https://github.com/googleapis/google-cloud-python/pull/7140))
- Protoc-generated serialization update. ([#7078](https://github.com/googleapis/google-cloud-python/pull/7078))
- Pick up stub docstring fix in GAPIC generator. ([#6966](https://github.com/googleapis/google-cloud-python/pull/6966))

## 0.2.1

12-17-2018 16:36 PST


### Documentation
- Document Python 2 deprecation ([#6910](https://github.com/googleapis/google-cloud-python/pull/6910))
- Improve linkage between container docs pages. ([#6852](https://github.com/googleapis/google-cloud-python/pull/6852))

### Internal / Testing Changes
- Add baseline for synth.metadata

## 0.2.0

12-04-2018 11:28 PST


### Implementation Changes
- Import `iam.policy` from `google.api_core.iam.policy` ([#6741](https://github.com/googleapis/google-cloud-python/pull/6741))
- Pick up fixes to GAPIC generator. ([#6634](https://github.com/googleapis/google-cloud-python/pull/6634))
- Fix `client_info` bug, update docstrings. ([#6407](https://github.com/googleapis/google-cloud-python/pull/6407))
- Avoid overwriting '__module__' of messages from shared modules. ([#5364](https://github.com/googleapis/google-cloud-python/pull/5364))
- Fix bad trove classifier

### Dependencies
- Bump minimum `api_core` version for all GAPIC libs to 1.4.1. ([#6391](https://github.com/googleapis/google-cloud-python/pull/6391))

### Documentation
- Docs: normalize use of support level badges ([#6159](https://github.com/googleapis/google-cloud-python/pull/6159))
- Container: harmonize / DRY 'README.rst' / 'docs/index.rst'. ([#6018](https://github.com/googleapis/google-cloud-python/pull/6018))
- Rename releases to changelog and include from CHANGELOG.md ([#5191](https://github.com/googleapis/google-cloud-python/pull/5191))

### Internal / Testing Changes
- Update noxfile.
- blacken all gen'd libs ([#6792](https://github.com/googleapis/google-cloud-python/pull/6792))
- Omit local dependencies from coverage. ([#6701](https://github.com/googleapis/google-cloud-python/pull/6701))
- Run black at end of synth.py ([#6698](https://github.com/googleapis/google-cloud-python/pull/6698))
- Unblack container gapic and protos.
- Run Black on Generated libraries ([#6666](https://github.com/googleapis/google-cloud-python/pull/6666))
- Add templates for flake8, coveragerc, noxfile, and black. ([#6642](https://github.com/googleapis/google-cloud-python/pull/6642))
- Pass posargs to py.test ([#6653](https://github.com/googleapis/google-cloud-python/pull/6653))
- Update synth.py yaml location ([#6480](https://github.com/googleapis/google-cloud-python/pull/6480))
- Use new Nox ([#6175](https://github.com/googleapis/google-cloud-python/pull/6175))
- Container: add 'synth.py'. ([#6084](https://github.com/googleapis/google-cloud-python/pull/6084))
- Nox: use inplace installs ([#5865](https://github.com/googleapis/google-cloud-python/pull/5865))
- Modify system tests to use prerelease versions of grpcio ([#5304](https://github.com/googleapis/google-cloud-python/pull/5304))
- Add Test runs for Python 3.7 and remove 3.4 ([#5295](https://github.com/googleapis/google-cloud-python/pull/5295))

## 0.1.1

### Dependencies

- Update dependency range for api-core to include v1.0.0 releases (#4944)

### Documentation

- Replacing references to `stable/` docs with `latest/`. (#4638)

### Testing and internal changes

- Re-enable lint for tests, remove usage of pylint (#4921)
- Normalize all setup.py files (#4909)
- nox unittest updates (#4646)

## 0.1.0

[![release level](https://img.shields.io/badge/release%20level-alpha-orange.svg?style&#x3D;flat)](https://cloud.google.com/terms/launch-stages)

Google Kubernetes Engine is a managed environment for deploying containerized
applications. It brings our latest innovations in developer productivity,
resource efficiency, automated operations, and open source flexibility to
accelerate your time to market.

PyPI: https://pypi.org/project/google-cloud-container/0.1.0/
