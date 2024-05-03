# netbox-devicetype-library

The NetBox community maintains a public library of models used to create NetBox devices.

This library is meant as an extension of the official library for devices that are NRK (Broadcast) specific and does 
not fit into the contributing guidelines of the official library.

## Compatibility

This library follows the official [netbox-community/devicetype-library](https://github.com/netbox-community/devicetype-library/)
definitions.

## Contributing

See CONTRIBUTING.md for more details on how to contribute.
This library is maintained by NRK and has focus on Broadcast devices.

## Data Validation / Commit Quality Checks

There are two ways this repo focuses on keeping quality device-type definitions:

- **Pre-Commit Checks** - Optional, but **highly recommended**, for helping to identify simple issues before committing. (trailing-whitespace, end-of-file-fixer, check-yaml, yamlfmt, yamllint)
    - Installation
        - Virtual Environment Route
            - It is recommended to create a virtual env for your repo (`python3 -m venv venv`)
            - Install the required pip packages (`pip install -r requirements.txt`)
            - Continue to the "Install `pre-commit` Hooks"
        - `pre-commit` Only Route
            - [Install pre-commit](https://pre-commit.com/#install) (`pip install pre-commit`)
        - Install `pre-commit` Hooks
            - To install the pre-commit script: `pre-commit install`
    - Usage & Useful `pre-commit` Commands
        - After staging your files with `git`, to run the pre-commit script on changed files: `pre-commit run`
        - To run the pre-commit script on all files: `pre-commit run --all`
        - To uninstall the pre-commit script: `pre-commit uninstall`
    - Learn more about [pre-commit](https://pre-commit.com/)
- **GitHub Actions** - Automatically run before a PR can be merged. Repeats yamllint & validates against NetBox Device-Type Schema.
