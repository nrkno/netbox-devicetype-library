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

## Development Setup

### Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) -- fast Python package manager
- [direnv](https://direnv.net/) -- automatic environment setup (recommended)

### Quick Start (with direnv)

```bash
git clone git@github.com:nrkno/netbox-devicetype-library.git
cd netbox-devicetype-library
direnv allow
```

That's it. `direnv` will automatically create a virtual environment, install dependencies, and set up pre-commit hooks.

### Quick Start (without direnv)

```bash
git clone git@github.com:nrkno/netbox-devicetype-library.git
cd netbox-devicetype-library
make install
make hooks
```

### Makefile Targets

Run `make help` to see all available targets:

| Target | Description |
|--------|-------------|
| `make install` | Create venv and install dependencies |
| `make hooks` | Install pre-commit git hooks |
| `make lint` | Run yamllint on device and module types |
| `make fmt` | Format YAML files with yamlfmt |
| `make test` | Run pytest (only changed files vs upstream) |
| `make validate` | Run all pre-commit hooks on all files |
| `make validate-all` | Run pytest on ALL files (full validation) |
| `make clean` | Remove venv, caches, and generated files |
| `make update-hooks` | Update pre-commit hooks to latest versions |

## Data Validation / Commit Quality Checks

There are two ways this repo focuses on keeping quality device-type definitions:

- **Pre-Commit Hooks** - Automatically run on `git commit` when set up via `direnv allow` or `make hooks`. Checks include trailing-whitespace, end-of-file-fixer, check-yaml, yamlfmt, yamllint, and pytest.
    - After staging your files with `git`, hooks run automatically on commit
    - To run manually on changed files: `pre-commit run`
    - To run on all files: `make validate`
    - Learn more about [pre-commit](https://pre-commit.com/)
- **GitHub Actions** - Automatically run before a PR can be merged. Repeats yamllint & validates against NetBox Device-Type Schema.
