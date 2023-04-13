{{cookiecutter.project_name}}
==============================
[//]: # (Badges)

| **Latest release** | [![Last release tag](https://img.shields.io/github/release-pre/{{cookiecutter.github_url}}.svg)](https://github.com/{{cookiecutter.github_url}}/releases) ![GitHub commits since latest release (by date) for a branch](https://img.shields.io/github/commits-since/{{cookiecutter.github_url}}/latest)  [![Documentation Status](https://readthedocs.org/projects/{{cookiecutter.repo_name}}/badge/?version=latest)](https://{{cookiecutter.repo_name}}.readthedocs.io/en/latest/?badge=latest)                                                                                                                                                                                                                        |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Status**         | [![GH Actions Status](https://github.com/{{cookiecutter.github_url}}/actions/workflows/{{cookiecutter._ci_name}}.yaml/badge.svg)](https://github.com/{{cookiecutter.github_url}}/actions?query=branch%3A{{cookiecutter._central_branch_name}}+workflow%3A{{cookiecutter._ci_name}}) [![codecov](https://codecov.io/gh/{{cookiecutter.github_url}}/branch/{{cookiecutter._central_branch_name}}/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_url}}/branch/{{cookiecutter._central_branch_name}}) [![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/{{cookiecutter.github_url}}.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/{{cookiecutter.github_url}}/context:python) |

{{cookiecutter.description}}

{{cookiecutter.project_name}} is bound by a [Code of Conduct](https://github.com/{{cookiecutter.github_url}}/blob/{{cookiecutter._central_branch_name}}/CODE_OF_CONDUCT.md).

### Installation

To build {{cookiecutter.project_name}} from source,
we highly recommend using virtual environments.
If possible, we strongly recommend that you use
[Anaconda](https://docs.conda.io/en/latest/) as your package manager.
Below we provide instructions both for `conda` and
for `pip`.

#### With conda

Ensure that you have [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed.

Create a virtual environment and activate it:

```
conda create --name {{cookiecutter.repo_name}}
conda activate {{cookiecutter.repo_name}}
```

Install the development and documentation dependencies:

```
conda env update --name {{cookiecutter.repo_name}} --file devtools/conda-envs/test_env.yaml
conda env update --name {{cookiecutter.repo_name}} --file docs/requirements.yaml
```

Build this package from source:

```
pip install -e .
```

If you want to update your dependencies (which can be risky!), run:

```
conda update --all
```

And when you are finished, you can exit the virtual environment with:

```
conda deactivate
```

#### With pip

To build the package from source, run:

```
pip install -e .
```

If you want to create a development environment, install
the dependencies required for tests and docs with:

```
pip install -e ".[test,doc]"
```

### Copyright

The {{cookiecutter.project_name}} source code is hosted at https://github.com/{{cookiecutter.github_url}}
and is available under the GNU General Public License, version 3 (see the file [LICENSE](https://github.com/{{cookiecutter.github_url}}/blob/{{cookiecutter._central_branch_name}}/LICENSE)).

Copyright (c) {% now 'utc', '%Y' %}, {{cookiecutter.author_name}}


#### Acknowledgements
 
Project based on the 
[OpenFF Cookiecutter](https://github.com/lilyminium/cookiecutter-openff) version {{cookiecutter._openff_cc_version}}.
