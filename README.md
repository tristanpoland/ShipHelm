<p align="center">
<img src="https://user-images.githubusercontent.com/34868944/223447636-3e17dee3-ccdf-44cc-8d42-91378ced6708.png" width="400" />
</p>

# Shiphelm

Shiphelm is a Python library for interacting with Docker containers more easily. With Shiphelm, you can:

- Get a list of all running containers
- Get usage statistics and used ports for a given container by ID
- Search containers by name or ID
- Change the open ports of a container
- Run new containers

## Installation

You can install Shiphelm using pip:

```pip install shiphelm```

## Usage

Here's an example of how to use Shiphelm to start an Nginx container on port 8181:

```python
import shiphelm

client = shiphelm.Client()

container = client.containers.run(
    image='nginx',
    ports={'80/tcp': 8181},
    detach=True
)```

Here's an example of how to use Shiphelm to get a list of all running containers:

```import shiphelm

client = shiphelm.Client()

containers = client.containers.list()
```

