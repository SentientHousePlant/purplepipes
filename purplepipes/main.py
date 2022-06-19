import click
from purplepipes.utils import parse_yaml

@click.group()
def cli():
    pass

@cli.command()
def run():
    print(parse_yaml())
    
