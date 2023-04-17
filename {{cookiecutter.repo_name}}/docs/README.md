# Compiling {{cookiecutter.project_name}}'s Documentation

The docs for this project are built with [Sphinx](http://www.sphinx-doc.org/en/master/).
To compile the docs, first install the documentation dependencies into a new environment called `{{cookiecutter.repo_name}}-docs`:

```bash
mamba env create -n {{cookiecutter.repo_name}}-docs -f ../devtools/conda-envs/docs_env.yaml 
```

Once installed, you can use Sphinx to render the docs:

```bash
mamba activate {{cookiecutter.repo_name}}-docs
make html
```

Or from the root directory of the repository, use `sphinx-build` directly:

```bash
sphinx-build -j auto docs docs/_build
```

The compiled docs will be in the `_build` directory and can be viewed by opening `index.html` (which may itself 
be inside a directory called `html/` depending on what version of Sphinx is installed).

A configuration file for [Read The Docs](https://readthedocs.org/) (readthedocs.yaml) is included in the top level of the repository. To use Read the Docs to host your documentation, go to https://readthedocs.org/ and connect this repository. You may need to change your default branch to `main` under Advanced Settings for the project.

If you would like to use Read The Docs with `autodoc` (included automatically) and your package has dependencies, you will need to include those dependencies in your documentation yaml file (`docs/requirements.yaml`).
