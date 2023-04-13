"""
Unit and regression test for the {{cookiecutter.package_name}} package.
"""

# Import package, test suite, and other packages as needed
import {{cookiecutter.package_name}}
import pytest
import sys


def test_{{cookiecutter.package_name}}_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "{{cookiecutter.package_name}}" in sys.modules


def test_molecule_charges(example_molecule_with_charges):
    """Example test using a fixture defined in conftest.py"""
    assert example_molecule_with_charges.partial_charges is not None
