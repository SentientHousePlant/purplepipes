import click
import jsonschema
from purplepipes.utils import parse_yaml
from purplepipes.constants import DEFAULT_PAML_NAME

@click.group()
def cli():
    pass

@cli.command()
def run():
    print(parse_yaml())
    
@cli.command()
def validate():
    try:
        parse_yaml()
        print(f"{DEFAULT_PAML_NAME} is a valid purplepipes config file.")
    except jsonschema.ValidationError() as e:
        print(f"Invalid Schema : {e}")
