import jsonschema

purple_yaml_schema = {
    "type" : "object",
    "properties" : {
        "name" : {"type":"string"},
        "input" : {"type":"string"},
        "steps" : {"type":"object"},
        "output" : {"type" : "string", "enum" : ["csv", "json"]},
        "output path" : {"type" : "string"}
    },
    "required":["name", "input", "output", "output path", "steps"]
}

if __name__ == "__main__":

    test_dict = {
        "name" : "test",
        "input" : "hi",
        "output" : "csv",
        "output path": "somewhere"
    }

    jsonschema.validate(schema=purple_yaml_schema, instance=test_dict)