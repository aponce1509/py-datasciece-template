import click

from {{ cookiecutter.__package_slug }} import __version__
from {{ cookiecutter.__package_slug }}..data.make_dataset import main as mk_dataset


@click.group()
@click.version_option(version=__version__)
def cli():
    pass


@cli.command()
def create_dataset():
    mk_dataset()