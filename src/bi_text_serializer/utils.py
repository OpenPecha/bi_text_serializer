from pathlib import Path
import yaml


def from_yaml(fn:Path):
    return yaml.safe_load(fn.read_text(encoding="utf-8"))

def to_yaml(data: dict):
    return yaml.safe_dump(data, default_flow_style=False,sort_keys=False,allow_unicode=True,)