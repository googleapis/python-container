# Samples

All the samples are self contained unless they are placed inside their own folders. The samples use [Application Default Credentails (ADC)](https://cloud.google.com/docs/authentication/production#automatically) to authenticate with GCP. So make sure ADC is setup correctly _(i.e. `GOOGLE_APPLICATION_CREDENTIALS` environment variable is set)_ before running the samples. Some sample might require additional python modules to be installed.

You can run samples as follows:

```python
python <sample_name.py> <arg1> <arg2> ...
```

You can run the following command to find the usage and arguments for the samples:

```python
python <sample_name.py> -h
```
```bash
# example
python quickstart.py -h

usage: quickstart.py [-h] project_id zone

positional arguments:
  project_id  Google Cloud project ID
  zone        GKE Cluster zone

optional arguments:
  -h, --help  show this help message and exit
```

- **quickstart.py**: A simple example to list the GKE clusters in a given GCP project and zone.

- **create_cluster.py**: An example of creating a GKE cluster _(with mostly the defaults)_. This example shows how to handle responses of type [`Operation`](https://cloud.google.com/python/docs/reference/container/latest/google.cloud.container_v1.types.Operation) that reperesents a long running operation. The example uses the python module [`backoff`](https://github.com/litl/backoff) to handle a graceful exponential backoff retry mechanism to check if the `Operation` has completed.

- **delete_cluster.py**: An example of deleting a GKE cluster. This example shows how to handle responses of type [`Operation`](https://cloud.google.com/python/docs/reference/container/latest/google.cloud.container_v1.types.Operation) that reperesents a long running operation.