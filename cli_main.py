#!/usr/bin/env python
import click
from internal.datastore.datastore_cmd import datastore_cmd
from internal.healthcheck.healthcheck_cmd import healthcheck_cmd
from internal.nested.nested_cmd import nested_group
from internal.version.version_cmd import version_cmd


@click.group()
def cli():
    pass


cli.add_command(datastore_cmd)
cli.add_command(healthcheck_cmd)
cli.add_command(nested_group)
cli.add_command(version_cmd)


if __name__ == "__main__":
    cli()