# Developer Guide

This guide intends to help you set up your local development environment and
give you directions on extending the module.

## Environment

### Prerequisites

- Python 3.10.1

### Set up local environment

Create a virtual environment and install all development dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Adding/Removing environment variables

When adding or removing environment variables, make sure to edit them in the following places:
1. `.env` in the root, which is not commited to the repository
2. `.env-template`, which is added to the repository
3. The `staging` and `production` environments of Prefect or Kafka. More information to be added in the future.

