import click
import shutil
import subprocess
import sys

from pathlib import Path


@click.group()
def cli():
    pass


@cli.command()
@click.argument("project_name")
def create(project_name):
    """Create a new skill using the default template."""
    pass


@cli.command()
def deploy():
    """Deploy a skill to AWS Lambda."""
    pass


@cli.command()
def build():
    """Build your skill to skill.zip including dependencies"""
    install_dependency("git+https://github.com/Lanseuo/alasan.git")
    install_requirements()
    shutil.copy("skill.py", ".alasan/build")

    shutil.make_archive("skill", 'zip', ".alasan/build")
    shutil.rmtree(".alasan/build")
    print("Created skill.zip")


def install_requirements():
    requirements_file = Path("requirements.txt")
    if not requirements_file.exists():
        return

    install_dependency(["-r", requirements_file])


def install_dependency(package):
    if isinstance(package, list):
        subprocess.check_call([sys.executable, "-m", "pip", "install", *package, "-t", ".alasan/build"])
    else:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, "-t", ".alasan/build"])
