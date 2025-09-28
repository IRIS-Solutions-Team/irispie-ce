#
# Print edition from pyproject.toml version
#

import toml

_PYPROJECT_PATH = "./pyproject.toml"
_EPOCH_SEPARATOR = "!"

_EPOCH_FROM_EDITION = {
    "de": "0",
    "ce": "1",
    "re": "2",
    "pe": "3",
}

edition_from_epoch = {
    v: k
    for k, v in _EPOCH_FROM_EDITION.items()
}

with open(_PYPROJECT_PATH, "rt") as f:
    toml_content = toml.load(f, )

version = toml_content["project"]["version"]
epoch, _, = version.rsplit(_EPOCH_SEPARATOR, maxsplit=1, )
edition = edition_from_epoch[epoch]
print(edition)

