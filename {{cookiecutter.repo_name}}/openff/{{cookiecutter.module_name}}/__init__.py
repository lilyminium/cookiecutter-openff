"""
{{cookiecutter.description}}
"""

# Add imports here
from .{{cookiecutter.module_name}} import canvas

# By default, imported items are not rendered in the docs unless they are
# included in __all__.
__all__ = [
    "canvas",
]

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions
