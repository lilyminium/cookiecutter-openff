
from .utils import CookiecutterOpenFF

def test_write_outputs(
    test_output_directory,
):
    
    description = (
        "Test OpenFF Project"
    )
    project_name = "test_openff"

    test_output_directory.mkdir(exist_ok=True)
    kitter = CookiecutterOpenFF(
        project_name=project_name,
        repo_name="openff-cookie",
        package_name="openff_cookie",
        github_username="test-user-account",
        github_host_account="openforcefield",
        description=description,
        output_directory=str(test_output_directory.resolve()),
    )
    kitter.run()