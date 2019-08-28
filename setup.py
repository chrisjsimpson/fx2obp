from setuptools import setup

setup(
  name="fx2obp",
  version='0.1',
  description="Convert exchange rates to OBP format, and optionally post to an OBP instance",
  url="https://github.com/chrisjsimpson/fx2obp",
  author="Chris Simpson",
  author_email="chris15leicester@gmail.com",
  classifiers=(
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU Affero General Public License v3",
    "Operating System :: OS Independent",
  ),
  packages=['fx2obp'],
  install_requires=[
    'bs4',
    'requests'
  ]
)
