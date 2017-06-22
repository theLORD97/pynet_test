#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals

import yaml
from pprint import pprint


def read_yaml(file):
    with open(file) as f:
        return yaml.load(f)

if __name__ == "__main__":
    file = "test_file.yaml"
    pprint(read_yaml(file))

 
