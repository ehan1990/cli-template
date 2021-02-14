import click
import json
import requests
from internal.common.constants import DEFAULT_TIMEOUT, ROOT_URL, VERSION


@click.group(name="nested")
def nested_group():
    pass


@nested_group.group(name="level1")
def nested_level_one_group():
    pass


@nested_level_one_group.command(name="insert")
def level_one_insert():
    print("level 1 insert")


@nested_group.group(name="level2")
def nested_level_two_group():
    pass


@nested_level_two_group.command(name="insert")
def level_two_insert():
    print("level 1 insert")
