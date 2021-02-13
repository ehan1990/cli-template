import click
import json
import requests
from internal.common.constants import DEFAULT_TIMEOUT, ROOT_URL, VERSION


@click.command(name="healthcheck")
@click.option("--json", "json_flag", default=False, is_flag=True)
def healthcheck_cmd(json_flag):
    res = requests.get(f"{ROOT_URL}/healthcheck", timeout=DEFAULT_TIMEOUT).json()
    if json_flag:
        print(json.dumps(res))
        return

    timestamp = res["timestamp"]
    api_version = res["version"]
    print(f"Timestamp: {timestamp}")
    print(f"Version: {api_version}")
