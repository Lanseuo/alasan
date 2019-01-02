import click
import os


@click.group()
def cli():
    pass


@cli.command()
@click.argument("project_name")
def create(project_name):
    """Create a new skill using the default template."""
    return


@cli.command()
def deploy():
    """Deploy a skill to AWS Lambda."""
    return
