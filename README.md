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

# Docker Usage

To use the SkiffUI library, you must first install the Docker SDK for Python:

`pip install docker` 

Once you have installed the Docker SDK, you can import the SkiffUI library and create a new instance of the `docker` class:

`from shiphelm import docker

docker = docker()` 

### Get a List of Running Containers

`running_containers = docker.get_running_containers()` 

### Get Stats and Ports for a Container by ID

`container_stats = docker.get_container_stats(container_id)
container_ports = docker.get_container_ports(container_id)` 

### Search for Containers by Name

`containers_by_name = docker.search_containers(name)` 

### Change the Ports of a Container

`docker.change_container_ports(container_id, ports)` 

### Rename a Container

`docker.rename_container(container_id, new_name)` 

### Add and Remove Containers from Networks

`docker.add_container_to_network(container_id, network_name)
docker.remove_container_from_network(container_id, network_name)` 

### Create and Delete Networks

`docker.create_network(network_name)
docker.delete_network(network_name)` 

### Run a New Container

`container = docker.run_container(
    image=image,
    command=command,
    detach=detach,
    ports=ports,
    environment=environment,
    volumes=volumes
)` 

### Get and Set Environment Variables for a Container

`container_environment = docker.get_container_environment(container_id)
docker.set_container_environment(container_id, environment)` 

### Get and Set Volumes for a Container

pythonCopy code

`container_volumes = docker.get_container_volumes(container_id)
docker.set_container_volumes(container_id, volumes)` 

# Contributing

If you would like to contribute to SkiffUI, please feel free to open a pull request or issue on the [GitHub repository](https://github.com/Gameplex-Software/SkiffUI).
