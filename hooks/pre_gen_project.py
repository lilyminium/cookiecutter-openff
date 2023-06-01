"""
Pre Cookie Generation script(s)

If any error is raised, the cookie cutter creation fails and crashes



=== VARIABLE INJECTION ===
This next section uses the fact that the script is rendered with Jinja
prior to execution to inject values into the template.

First it normalizes the project name so we can seperate the "OpenFF" prefix from
the name of the project. This logic allows the package name to conform to OpenFF
conventions even if the user inputs something wierd, like using a dash instead
of a space or using unusual capitalisation:

{%- if cookiecutter.project_name.lower().replace(' ', '-').replace('-', '-').startswith('openff-') -%}
    {{ cookiecutter.update({"project_name_short": cookiecutter.project_name[7:]}) }}
{%- else -%}
    {{ cookiecutter.update({"project_name_short": cookiecutter.project_name}) }}
{%- endif -%}

Then it assigns the normalized project name, package name (name of the Conda
Forge package), module name (name of the Python module within the ``openff``
namespace), and import path based on the slug generated in
``cookiecutter.json`` and validated below:

{{ cookiecutter.update({
    "project_name": "OpenFF " ~ cookiecutter.project_name_short,
    "package_name": cookiecutter.repo_name,
    "module_name": cookiecutter.repo_name[7:],
    "import_path": "openff." ~ cookiecutter.repo_name[7:],
}) }}

Next it checks to see if the `github_host_account` is the default value,
i.e. the instructional help text. If so, it replaces the value with
`github_username`:

{{ cookiecutter.update({"github_host_account": cookiecutter.github_host_account | trim }) }}

{% if (not cookiecutter.github_host_account or "organization account" in cookiecutter.github_host_account) %}
    {{ cookiecutter.update({ "github_host_account": cookiecutter.github_username }) }}
{% else %}
    {{ cookiecutter.update({ "github_host_account": cookiecutter.github_host_account }) }}
{% endif %}

Finally, it adds a `github_url` variable for easier use with CI, etc:

{{ cookiecutter.update({"github_url": [cookiecutter.github_host_account, cookiecutter.repo_name]|join("/") }) }}


=== LICENSE ===

{{ cookiecutter.update({"open_source_license": 'MIT'}) }}

"""

import re
import sys
import os

REGEX_EMAIL = r"^[^@]+@[^@]+\.[^@]+$"
REGEX_URL_COMPATIBLE = r"^[_\-a-zA-Z][_\-a-zA-Z0-9]+$"
REGEX_PYTHON_COMPATIBLE = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
OPENFF_REPO_NAME = r"^openff-[_\-a-z0-9]+$"


def validate(regex: str, value: str, field: str, allow_empty: bool = False):
    if allow_empty and not value:
        return
    if not re.match(regex, value):
        print(f"ERROR: '{value}' is not a valid {field}! Should match regex '{regex}'.")

        # exits with status 1 to indicate failure
        sys.exit(1)


if __name__ == "__main__":
    validate(REGEX_EMAIL, "{{ cookiecutter.author_email }}", "email")
    validate(REGEX_URL_COMPATIBLE, "{{ cookiecutter.repo_name }}", "repo name")
    validate(
        REGEX_URL_COMPATIBLE, "{{ cookiecutter.github_username }}", "GitHub username"
    )
    validate(
        REGEX_URL_COMPATIBLE, "{{ cookiecutter.github_host_account }}", "GitHub account"
    )
    validate(REGEX_PYTHON_COMPATIBLE, "{{ cookiecutter.module_name }}", "module name")
    validate(OPENFF_REPO_NAME, "{{ cookiecutter.repo_name }}", "repo name")
    print(f"\nCreating '{{ cookiecutter.project_name }}' in {os.getcwd()}")
