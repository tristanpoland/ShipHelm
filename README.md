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

```
pip install shiphelm
```
PyPI: [https://pypi.org/project/Shiphelm/]()

GitHub Releases [https://github.com/Gameplex-Software/ShipHelm/releases]()

## Docker usage

```
from shiphelm.helmdocker import helmdocker

hd = helmdocker() # create an instance of helmdocker
```

### Get a List of Running Containers

```
running_containers = hd.get_running_containers()
``` 

### Get Stats and Ports for a Container by ID

```
container_stats = hd.get_container_stats(container_id)
container_ports = hd.get_container_ports(container_id)
```

### Search for Containers by Name

```
containers_by_name = hd.search_containers(name)
``` 

### Change the Ports of a Container

```
hd.change_container_ports(container_id, ports)
``` 

### Rename a Container

```
hd.rename_container(container_id, new_name)
``` 

### Add and Remove Containers from Networks

```
hd.add_container_to_network(container_id, network_name)
hd.remove_container_from_network(container_id, network_name)
``` 

### Create and Delete Networks

```
hd.create_network(network_name)
hd.delete_network(network_name)
``` 

### Run a New Container

```
container = hd.run_container(
    image=image,
    command=command,
    detach=detach,
    ports=ports,
    environment=environment,
    volumes=volumes
)
``` 

### Get and Set Environment Variables for a Container

```
container_environment = hd.get_container_environment(container_id)
hd.set_container_environment(container_id, environment)
``` 

### Get and Set Volumes for a Container

pythonCopy code

```
container_volumes = hd.get_container_volumes(container_id)
hd.set_container_volumes(container_id, volumes)
``` 

# Contributing

If you would like to contribute to SkiffUI, please feel free to open a pull request or issue on the [GitHub repository](https://github.com/Gameplex-Software/SkiffUI).
