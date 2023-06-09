# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Installing {{cookiecutter.project_name}}

OpenFF recommends using Conda virtual environments for all scientific Python work. {{cookiecutter.project_name_short}} can be installed into a new Conda environment named `{{cookiecutter.module_name}}` with the [`{{cookiecutter.package_name}}`] package:

```shell-session
$ mamba create -n {{cookiecutter.module_name}} -c conda-forge {{cookiecutter.package_name}}
$ mamba activate {{cookiecutter.module_name}}
```

If you do not have Conda or Mamba installed, see the [OpenFF installation documentation](inv:openff.docs#install).

[`{{cookiecutter.package_name}}`]: https://anaconda.org/conda-forge/{{cookiecutter.package_name}}

:::{toctree}
---
hidden: true
---

Overview <self>
:::

<!--
The autosummary directive renders to rST,
so we must use eval-rst here
-->
```eval-rst
.. raw:: html

    <div style="display: None">

.. autosummary::
   :recursive:
   :caption: API Reference
   :toctree: api/generated
   :nosignatures:

   {{cookiecutter.import_path}}

.. raw:: html

    </div>
```
