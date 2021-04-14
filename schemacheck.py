#!/usr/bin/env python3

import argparse
import json
import logging
import sys

import jsonschema
import yaml

SCHEMA_VERSIONS = ["2020-12", "draft-07"]

SCHEMATA = {
    "2020-12": "http://json-schema.org/draft/2020-12/schema#",
    "draft-07": "http://json-schema.org/draft-07/schema#",
}

SCHEMA_VERSIONS = list(SCHEMATA.keys())

DRAFT_07_KEYS = [
    "example",
    "minimum",
    "maximum",
]


def filter_schema(node, version: str):
    if isinstance(node, dict):
        res = node.copy()
        for k, v in node.items():
            if version == "draft-07":
                if k == "$schema":
                    res[k] = "http://json-schema.org/draft-07/schema#"
                elif k in DRAFT_07_KEYS:
                    del res[k]
                else:
                    res[k] = filter_schema(v, version)
            else:
                res[k] = filter_schema(v, version)
        return res
    return node


def main():
    """ Main function"""

    parser = argparse.ArgumentParser(description="Schema checker")
    parser.add_argument("schema", metavar="filename")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--input", metavar="filename")
    parser.add_argument(
        "--version",
        metavar="version",
        default=SCHEMA_VERSIONS[0],
        choices=SCHEMA_VERSIONS,
    )
    args = parser.parse_args()

    filename = args.schema

    with open(filename) as file:
        print("Checking schema", filename, file=sys.stderr)
        if filename.endswith(".json"):
            schema = json.load(file)
        elif filename.endswith(".yaml"):
            schema = yaml.load(file, Loader=yaml.SafeLoader)
        else:
            raise Exception("Unknown schema format")

    schema = filter_schema(schema, args.version)
    jsonschema.Draft4Validator.check_schema(schema)

    if args.json:
        print(json.dumps(schema, indent=4))

    if args.input:
        with open(args.input) as file:
            print("Checking input", args.input, file=sys.stderr)
            if args.input.endswith(".json"):
                data = json.load(file)
            elif args.input.endswith(".yaml"):
                data = yaml.load(file, Loader=yaml.SafeLoader)
            else:
                raise Exception("Unknown input format")
            jsonschema.validate(data, schema)


if __name__ == "__main__":
    main()
