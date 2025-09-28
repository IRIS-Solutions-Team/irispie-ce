#
# Print mmp from pyproject.toml version
#

import toml

_PYPROJECT_PATH = "./pyproject.toml"
_EPOCH_SEPARATOR = "!"

with open(_PYPROJECT_PATH, "rt") as f:
    toml_content = toml.load(f, )

version = toml_content["project"]["version"]
_, mmp, = version.rsplit(_EPOCH_SEPARATOR, maxsplit=1, )
print(mmp)

