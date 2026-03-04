r"""
"""


import importlib.metadata as _md
import re as _re
import functools as _ft
import warnings as _wa
from pathlib import Path


_BANNERS = {
    "de": (
        "\n\n"
        "=================================================================\n"
        " You are using IrisPie Developer Edition.\n"
        " This edition is intended for development and testing only.\n"
        " It may be used solely by registered developers.\n"
        " Contact info@ogresearch.com for more information.\n"
        "=================================================================\n\n"
    ),
    "ce": (
        "\n\n"
        "=================================================================\n"
        " You are using IrisPie Community Edition.\n"
        " Free for personal, educational, and non-commercial use only.\n"
        " Registration is required for commercial or institutional use.\n"
        " Contact info@ogresearch.com for more information.\n"
        "=================================================================\n\n"
    ),
    "re": (
        "\n\n"
        "=================================================================\n"
        " You are using IrisPie Registered Edition.\n"
        " Licensed for use by organizations that have completed\n"
        " registration with OGResearch.\n"
        " Internal use and redistribution within the organization\n"
        " are permitted. External redistribution is prohibited.\n"
        " Contact info@ogresearch.com for more information.\n"
        "=================================================================\n\n"
    ),
    "pe": None,
}

package_name = Path(__file__).parent.name
editions = set(_BANNERS.keys())
joined_editions = "|".join(editions)
pattern = _re.compile(f"{package_name}-({joined_editions})$", )

distribution_generator = (
    i for i in _md.distributions()
    if pattern.match(i.name, )
)
distribution = next(distribution_generator, None, )

if not distribution:
    raise Exception(f"Cannot determine the {package_name} distribution", )

metadata = distribution.metadata
edition = metadata["name"][-2:]
__doc__ = metadata["description"]
__version__ = metadata["version"]


banner = _BANNERS[edition]
if banner:
    irispie_edition_warning = _ft.partial(_wa.warn, banner, UserWarning, )
else:
    def irispie_edition_warning():
        pass


def min_version_required(
    min_version_string: str,
):
    r"""
    Check if the current version of the package is greater than or equal to the minimum version required.
    """
    current_version = _convert_version(__version__, )
    minimum_version = _convert_version(min_version_string, )
    if current_version < minimum_version:
        raise Exception(
            f"Current version of {package_name} ({__version__}) is less than the minimum version required ({min_version_string})"
        )


def _convert_version(version_str: str) -> tuple[int, ...]:
    return tuple(int(s) for s in version_str.split("."))

