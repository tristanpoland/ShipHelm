<p align="center">
<a href="https://gameplex-software.github.io/ShipHelm/">
<img src="https://user-images.githubusercontent.com/34868944/223447636-3e17dee3-ccdf-44cc-8d42-91378ced6708.png" width="400" />
</a>
</p>

# Shiphelm

Shiphelm is a Python library for interacting with containers more easily. With Shiphelm, you can:

- Get a list of all running containers
- Get usage statistics and used ports for a given container by ID
- Search containers by name or ID
- Change the open ports of a container
- Run new containers
- Work with Docker, Docker-Swarm, and Kubernetes
- Use Kubernetes clusters and Docker Swarm

## Installation

You can install Shiphelm using pip:

```
pip install shiphelm
```
PyPI: [https://pypi.org/project/Shiphelm/]()

GitHub Releases [https://github.com/Gameplex-Software/ShipHelm/releases]()

## Docker usage

This code will allow you to manage the local container engine

```
from shiphelm.helm import helm

hd = helm.helm() # create an instance of helm
```

This code will allow you to manage any compatible remote container engine
```
from shiphelm.helm import helm

hd = helm.reomte_connect('tcp://remote-docker-host:2375') # create an instance of helmdocker for romote management
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

```
container_volumes = hd.get_container_volumes(container_id)
hd.set_container_volumes(container_id, volumes)
```
### Example code
This example runs 4 instances of the Docker "Getting Started" container

```
from shiphelm.helmdocker import helmdocker

hd = helmdocker() # create an instance of helmdocker
container_list = hd.get_running_containers() # call the method on the instance
print(container_list)
w=0

print("Preparing new server...")
while w<3:
    hd.run_container(image="docker/getting-started", detach=1)
    w=w+1

print("Your server is up and ready for connection!")
```


# Contributing

If you would like to contribute to SkiffUI, please feel free to open a pull request or issue on the [GitHub repository](https://github.com/Gameplex-Software/SkiffUI).
