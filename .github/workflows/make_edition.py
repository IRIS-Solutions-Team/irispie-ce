#
# Change edition in pyproject.toml
#

import argparse
import toml

_PYPROJECT_PATH = "./pyproject.toml"
_PROJECT_EDITION_SEPARATOR = "-"

_LICENSES = {
    "de": "OGResearch Developer License 1.0",
    "ce": "OGResearch Community License 1.0",
    "re": "OGResearch Registered License 1.0",
    "pe": "OGResearch Private License 1.0",
}

parser = argparse.ArgumentParser()
parser.add_argument("--edition", required=True, help="New edition to set (e.g., 'ce', 'de')")
args = parser.parse_args()

with open(_PYPROJECT_PATH, "rt") as f:
    toml_content = toml.load(f, )

current_name = toml_content["project"]["name"]
project_name, current_edition, = current_name.rsplit(_PROJECT_EDITION_SEPARATOR, maxsplit=1, )
new_name = f"{project_name}{_PROJECT_EDITION_SEPARATOR}{args.edition}"
toml_content["project"]["name"] = new_name

licence_name = _LICENSES[args.edition]
toml_content["project"]["license"] = {"text": licence_name}

with open(_PYPROJECT_PATH, "wt") as f:
    f.write(toml.dumps(toml_content, ), )

