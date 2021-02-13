import click
import json
import requests
from internal.common.constants import DEFAULT_TIMEOUT, ROOT_URL, VERSION


@click.group(name="datastore")
def datastore_cmd():
    pass


@datastore_cmd.command(name="insert")
@click.option("--value", required=True, type=int)
def insert_datastore_cmd(value):
    res = requests.post(f"{ROOT_URL}/example", json={"val": value}, timeout=DEFAULT_TIMEOUT)
    if res.status_code == 200:
        print(f"successfully inserted value {value}")
        return
    print(f"unable to insert value {value}")


@datastore_cmd.command(name="list")
def list_datastore_cmd():
    res = requests.get(f"{ROOT_URL}/example", timeout=DEFAULT_TIMEOUT)
    if res.status_code == 200:
        print(f"{res.json()}")
        return
    print(f"unable to list values from datastore")
