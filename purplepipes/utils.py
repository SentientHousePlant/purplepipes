from functools import partial
import jsonschema
from purplepipes.constants import DEFAULT_PAML_NAME
from purplepipes.constants import test_paml_schema
from yaml import safe_load

paml_validate = partial(jsonschema.validate, schema=test_paml_schema)

def parse_yaml(file_name=DEFAULT_PAML_NAME):
    with open(file_name) as paml:
        loaded_yaml = safe_load(paml)
    try:
        paml_validate(instance=loaded_yaml)
        return loaded_yaml
    except jsonschema.ValidationError as e:
        return e

    

    