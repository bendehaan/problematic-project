# Problematic project

Contains bad Python code with weak configuration settings, a sub-standard Dockerfile and vulnerable dependencies for demo purposes.

_**Don't run this thing in production.**_ 🙄

Based on the vulnerable Python webapp [Vulpy](https://github.com/fportantier/vulpy/) created by F. Portantier.

## Installing dependencies

`uv sync`

## Running the application

1. `uv run python db_init.py`
2. `uv run python ./vulpy.py`
