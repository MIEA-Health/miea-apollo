# MIEA Apollo

A python backend used to fetch data from facebook messenger and typeform for the purpose of data analysis and eventual storage into [`apollo-data`](https://github.com/MIEA-Health).
The package has been tested with Python 3.10.0.

## Quickstart

To run a sync script, first create a virtual environment, activate it and install the package

Mac / Linux
```console
python3 -m venv venv
source venv/bin/activate
pip3 install -e .
```

Windows
```console
python3 -m venv venv
venv/Scripts/activate
pip3 install -e .
```

Install pre-commit git hooks scripts
```console
pre-commit install
```

Set the environment variables by copying the `.env-template` and filling it

```console
cp .env-template .env
```

> Get values from Josh (pending integration into password manager)

And finally, run all scripts with

## TODO: add in script run framework here

## TODO: All scripts
```console
python3 -m 
```

## TODO: one script and docker
Optionally, run for a single provider with

```console
python3 -m 
```



## Troubleshooting Linux
Tested on Ubuntu 20.04.3 LTS
* Make sure you are on Python3.9.x and above

If this fails `python3 -m venv venv` with an error that looks like 
```
Error: Command '['/path/to/venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1.
```
You may need to run
```
python3 -m venv --without-pip venv
```
and install pip in your venv manually. In my case I had pip3 installed on my machine already, and pip worked in the venv fine.

Then if this fails `pip3 install -e .`

You may need to run
```shell
sudo apt update
sudo apt install python3-dev
sudo apt install libpython3.9-dev
```

## Development

For instructions on local development, see the [Developer Guide](./docs/DEVELOPER_GUIDE.md).

## Testing

For testing we use `pytest`. You can run all tests with

```console
pytest .
```

## Resources

- [Prefect Cloud](https://docs.prefect.io/concepts/states/)
- [Snowflake Kafka Connector](https://docs.snowflake.com/en/user-guide/kafka-connector-overview.html)
- [Kubernetes](https://kubernetes.io/docs/setup/)
- [Data Modelling](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/)
