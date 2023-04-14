import ast
import enum
from dataclasses import dataclass, asdict
import pathlib
from typing import Literal, List

from cookiecutter.main import cookiecutter

COOKIECUTTER_PATH = pathlib.Path(__file__).parent.parent.resolve()


@dataclass
class CookiecutterOpenFF:
    project_name: str = "TestOpenFFProjectName"
    repo_name: str = "test-openff-cookie"
    package_name: str = "test_openff_cookie"
    github_username: str = "test-user-account"
    github_host_account: str = "test-github-host-account"
    author_name: str = "Test User name"
    author_email: str = "test_email@test.com"
    description: str = "Test OpenFF Project description"
    output_directory: str = "."

    @property
    def cookie_directory(self) -> pathlib.Path:
        return pathlib.Path(self.repo_name)

    @property
    def package_directory(self) -> pathlib.Path:
        return self.cookie_directory / self.package_name

    def run(self):
        context = {}
        for k, v in asdict(self).items():
            if isinstance(v, enum.Enum):
                v = v.value
            context[k] = v

        return cookiecutter(
            str(COOKIECUTTER_PATH),
            no_input=True,
            extra_context=context,
            output_dir=self.output_directory,
        )

    def cookie_path_exists(self, path: str) -> bool:
        path = self.cookie_directory / path
        return path.exists()

    def cookie_package_path_exists(self, path: str) -> bool:
        path = self.package_directory / path
        return path.exists()
