#
# Change edition in pyproject.toml
#

import argparse
import toml

_PYPROJECT_PATH = "./pyproject.toml"
_VERSION_EDITION_SEPARATOR = "+"
_PROJECT_EDITION_SEPARATOR = "-"

_LICENSES = {
    "de": "OGResearch Developer License 1.0",
    "ce": "OGResearch Community License 1.0",
    "re": "OGResearch Registered License 1.0",
    "pe": "OGResearch Private License 1.0",
}

def _change_edition_in_string(
    current_string: str,
    new_edition: str,
    separator: str,
) -> str:
    whatever_before, *_ = current_string.rsplit(separator, maxsplit=1, )
    return f"{whatever_before}{separator}{new_edition}"

parser = argparse.ArgumentParser()
parser.add_argument("--edition", required=True, help="New edition to set (e.g., 'ce', 'de')")
args = parser.parse_args()

with open(_PYPROJECT_PATH, "rt") as f:
    toml_content = toml.load(f, )

current_version = toml_content["project"]["version"]
new_version = _change_edition_in_string(
    current_version,
    args.edition,
    _VERSION_EDITION_SEPARATOR,
)
toml_content["project"]["version"] = new_version

current_name = toml_content["project"]["name"]
new_name = _change_edition_in_string(
    current_name,
    args.edition,
    _PROJECT_EDITION_SEPARATOR,
)
toml_content["project"]["name"] = new_name

licence_name = _LICENSES[args.edition]
toml_content["project"]["license"] = {"text": licence_name}

with open(_PYPROJECT_PATH, "wt") as f:
    f.write(toml.dumps(toml_content, ), )

