from setuptools import setup
import re

with open("src/jinja2/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read(), re.M).group(1)

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="Smart-Invest",
    version=version,
)
