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
)
```

# Usage

To use the SkiffUI library, you must first install the Docker SDK for Python:

Copy code

`pip install docker` 

Once you have installed the Docker SDK, you can import the SkiffUI library and create a new instance of the `Client` class:

pythonCopy code

`from shiphelm import Client

client = Client()` 

### Get a List of Running Containers

pythonCopy code

`running_containers = client.get_running_containers()` 

### Get Stats and Ports for a Container by ID

pythonCopy code

`container_stats = client.get_container_stats(container_id)
container_ports = client.get_container_ports(container_id)` 

### Search for Containers by Name

pythonCopy code

`containers_by_name = client.search_containers(name)` 

### Change the Ports of a Container

pythonCopy code

`client.change_container_ports(container_id, ports)` 

### Rename a Container

pythonCopy code

`client.rename_container(container_id, new_name)` 

### Add and Remove Containers from Networks

pythonCopy code

`client.add_container_to_network(container_id, network_name)
client.remove_container_from_network(container_id, network_name)` 

### Create and Delete Networks

pythonCopy code

`client.create_network(network_name)
client.delete_network(network_name)` 

### Run a New Container

pythonCopy code

`container = client.run_container(
    image=image,
    command=command,
    detach=detach,
    ports=ports,
    environment=environment,
    volumes=volumes
)` 

### Get and Set Environment Variables for a Container

pythonCopy code

`container_environment = client.get_container_environment(container_id)
client.set_container_environment(container_id, environment)` 

### Get and Set Volumes for a Container

pythonCopy code

`container_volumes = client.get_container_volumes(container_id)
client.set_container_volumes(container_id, volumes)` 

# Contributing

If you would like to contribute to SkiffUI, please feel free to open a pull request or issue on the [GitHub repository](https://github.com/Gameplex-Software/SkiffUI).
