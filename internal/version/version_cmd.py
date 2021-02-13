import json
import click
from internal.common.constants import VERSION


@click.command(name="version")
@click.option("--json", "json_flag", default=False, is_flag=True)
def version_cmd(json_flag):
    if json_flag:
        print(json.dumps({"version": VERSION}))
        return
    print(f"CLI Template version: {VERSION}")
