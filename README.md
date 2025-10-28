# risk_tribe

CI/CD

## Project structure

The directory structure of the project looks like this:
```txt
├── .github/                  # Github actions and dependabot
│   ├── dependabot.yaml
│   └── workflows/
│       ├── linting.yaml
│       ├── pre-commit-update.yaml
│       ├── deploy.yaml       # if aws is chosen
│       └── tests.yaml

├── configs/                  # Configuration files
├── logs/                     # Log outputs, if logging is chosen
├── data/                     # Data directory
├── dockerfiles/              # Dockerfiles
│   ├── api.Dockerfile
│   └── train.Dockerfile
├── docs/                     # Documentation
│   ├── mkdocs.yml
│   └── source/
│       └── index.md
├── notebooks/                # Jupyter notebooks
├── infra/                    # deployment infrastrucure, if aws is chosen
│   ├── terraform
│       ├── main.tf
│       ├── outputs.tf
│       └── variables.tf
├── reports/                  # Reports
│   └── figures/
├── src/                      # Source code
│   ├── project_name/
│   │   ├── __init__.py
│   │   └── main.py
└── tests/                    # Tests
│   ├── __init__.py
│   ├── test_file.py
├── .gitignore
├── .pre-commit-config.yaml
├── LICENSE
├── pyproject.toml            # Python project file
├── README.md                 # Project README
├── requirements.txt          # Project requirements
├── requirements_dev.txt      # Development requirements
└── tasks.py                  # Project tasks
```


Created using [python mlops template](https://github.com/AndersHenriksen-dev/python_mlops_cookiecutter_template),
a [cookiecutter template](https://github.com/cookiecutter/cookiecutter) for getting started with python and CI/CD.
