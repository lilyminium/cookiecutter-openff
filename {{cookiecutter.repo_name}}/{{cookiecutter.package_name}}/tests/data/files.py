"""
Location of data files for tests
================================

Use as ::

    from {{ cookiecutter.package_name }}.tests.data.files import EXAMPLE_SDF_WITH_CHARGES
    from openff.toolkit import Molecule

    molecule = Molecule.from_file(EXAMPLE_SDF_WITH_CHARGES.resolve(), file_format="sdf")

"""

__all__ = [
    "EXAMPLE_SDF_WITH_CHARGES",
]

import importlib

data_directory = importlib.resources.files(
    "{{ cookiecutter.package_name }}") / "tests" / "data"

EXAMPLE_SDF_WITH_CHARGES = data_directory / "C1CC1.sdf"
