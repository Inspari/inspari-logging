This repository provides Python logging utilities.

### Installation

#### Poetry

To install the package, add the following to your `pyproject.toml` file,

```toml
[tool.poetry.dependencies]
inspari-logging = { git = "git@ssh.dev.azure.com:v3/Inspari-Accelerators/Accelerators/inspari-logging" }
```

You will need an access token for:
```
https://Inspari-Accelerators@dev.azure.com/Inspari-Accelerators
```


### Configuration

The `inspari.logging` module provides unified interface for loading logging configuration files in app code and from 
gunicorn. In addition, a range of utilities (service name prefixing, command line colors etc.) are provided. 

An example logging configuration file is bundled (`example_logging_config.json`), along with an example of the usage in 
an application context (`example_usage.py`).

### Stream logs

The streamlogs command line utility provides a simple way to stream logs in _realtime_. To enable log collection, add a 
handler as part of your logging configuration,

```json
    "handlers": {
        "web": {
            "class": "inspari.logging.AzureBlobStorageHandler",
            "formatter": "simple",
            "load_dot_env": "true",
            "env_key": "ABS_CONNECTION_STRING",
            "log_local": "true"
        },
        ...
    },
    ...
    "root": {
        "level": "INFO",
        "handlers": [
            "web",
            ...
        ]
    },
```

and configure the logs as demonstrated in `example_usage.py`. The storage account to use for streaming must be specified
via environment variables. In the example case, a connection string is used. Hence, for local development purposes, 
it is recommended to create a .env file with the content like,

```bash
ABS_CONNECTION_STRING=REDACTED
```

Note that by default, logs are written to container called `logs`, so you must create a container with this name,
if it doesn't already exist. If you now run,

```bash
poetry run steamlogs
```

you should be getting logs in (near) realtime from all services connected to the account.