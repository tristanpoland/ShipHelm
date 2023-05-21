<p align="center">
<a href="https://gameplex-software.github.io/ShipHelm/">
<img src="https://user-images.githubusercontent.com/34868944/223447636-3e17dee3-ccdf-44cc-8d42-91378ced6708.png" width="400" />
</a>
</p>

# Shiphelm

## Table of Contents

- [Shiphelm](#shiphelm)
  - [Installation](#installation)
  - [Docker usage example](#docker-usage-example)
    - [Get a List of Running Containers](#get-a-list-of-running-containers)
    - [Get a running container by ID](#get-a-running-container-by-id)
    - [Get Stats and Ports for a Container by ID](#get-stats-and-ports-for-a-container-by-id)
    - [Search for Containers by Name](#search-for-containers-by-name)
    - [Change the Ports of a Container](#change-the-ports-of-a-container)
    - [Rename a Container](#rename-a-container)
    - [Add and Remove Containers from Networks](#add-and-remove-containers-from-networks)
    - [Create and Delete Networks](#create-and-delete-networks)
    - [Run a New Container](#run-a-new-container)
    - [Get and Set Environment Variables for a Container](#get-and-set-environment-variables-for-a-container)
    - [Get and Set Volumes for a Container](#get-and-set-volumes-for-a-container)
    - [Example code](#example-code)
  - [Kubernetes (K8S) usage example](#kubernetes-k8s-usage-example)
    - [Get a List of Running Containers](#get-a-list-of-running-containers-1)
    - [Get Stats and Ports for a Container by ID](#get-stats-and-ports-for-a-container-by-id-1)
    - [Search for Containers by Name](#search-for-containers-by-name-1)
    - [Change the Ports of a Container](#change-the-ports-of-a-container-1)
    - [Rename a Container](#rename-a-container-1)
    - [Add and Remove Containers from Networks](#add-and-remove-containers-from-networks-1)
    - [Create and Delete Networks](#create-and-delete-networks-1)
    - [Run a New Container](#run-a-new-container-1)
    - [Get and Set Environment Variables for a Container](#get-and-set-environment-variables-for-a-container-1)
    - [Get and Set Volumes for a Container](#get-and-set-volumes-for-a-container-1)
    - [Example code](#example-code-1)
    - [Dynamic engine selection](#dynamic-engine-selection)
    - [Remote engines via GUI](#remote-engines-via-gui)
- [Contributing](#contributing)


Shiphelm is a Python library for interacting with containers more easily. With Shiphelm, you can:

- Get a list of all running containers
- Get usage statistics and used ports for a given container by ID
- Search containers by name or ID
- Change the open ports of a container
- Run new containers
- Work with Docker, and Kubernetes
- Use Kubernetes clusters and Docker Swarm
- work on clusters, and swarms of container hosts

## Installation

You can install Shiphelm using pip:

```
pip install shiphelm
```
PyPI: [https://pypi.org/project/Shiphelm/]()

GitHub Releases [https://github.com/Gameplex-Software/ShipHelm/releases]()


<p align="center">
<img src="https://user-images.githubusercontent.com/34868944/231290469-900a253f-1236-4dd3-a126-85177931ce53.png" width="1000" />
</p>

## Docker usage example

This code will allow you to manage the local container engine


### Standalone Docker installation
```
from shiphelm.helm import helm

hd = helm() # create an instance of helm

helm.set_engine_manual("docker")
```

### Remote standalone Docker installation

This code will allow you to manage any compatible remote container engine
```
from shiphelm.helm import helm

hd = helm.reomte_connect('tcp://remote-docker-host:2375') # create an instance of helmdocker for romote management
```

### Remote Docker swarm installation

```
from shiphelm.helm import helm

hd = helm.helm() # create an instance of helm

helm.set_engine_manual(engine_select="docker", remoteAddress="YOUR ADDRESS HERE", remoteSecurity=<True|False>)
```

### Get a List of Running Containers

```
running_containers = hd.get_running_containers()
``` 

### Get a running container by ID

```
get_container_by_id(container_id)
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

### Generate run command
ShipHelm is capable of retrieving your container's inspect data and re-creating the original command that was used to run your pod, allowing you to re-create it anywhere

```
container_name = "your_container_name"
namespace = "your_namespace"  # Default is "default"
run_command = get_kubernetes_run_command(pod_name, namespace)
print(f"Run command for pod {pod_name} in namespace {namespace}: {run_command}")
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

<p align="center">
<img src="https://user-images.githubusercontent.com/34868944/231290322-e18c1082-89e2-4b8a-abb3-8aee93f57bf9.png" width="1000" />
</p>

## Kubernetes (K8S) usage example

This code will allow you to manage the local container engine

```
from shiphelm.helm import helm

hd = helm.helm() # create an instance of helm

helm.set_engine_manual("kubernetes")
```

This code will allow you to manage any compatible remote container engine
```
from shiphelm.helm import helm

hd = helm.reomte_connect('tcp://remote--host:2375') # create an instance of helm for romote management
```

### Get a List of Running pods

```
running_containers = hd.get_running_containers()
``` 

### Get Stats and Ports for a pod by ID

```
container_stats = hd.get_container_stats(container_id)
container_ports = hd.get_container_ports(container_id)
```

### Search for pods by Name

```
containers_by_name = hd.search_containers(name)
``` 

### Change the Ports of a pod

```
hd.change_container_ports(container_id, ports)
``` 

### Rename a pod

```
hd.rename_container(container_id, new_name)
``` 

### Add and Remove pods from Networks

```
hd.add_container_to_network(container_id, network_name)
hd.remove_container_from_network(container_id, network_name)
``` 

### Create and Delete Networks

```
hd.create_network(network_name)
hd.delete_network(network_name)
``` 

### Run a New pod

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

### Generate run command
ShipHelm is capable of retrieving your pod's inspect data and re-creating the original command that was used to run your pod, allowing you to re-create it anywhere

```
pod_name = "your_pod_name"
namespace = "your_namespace"  # Default is "default"
run_command = get_kubernetes_run_command(pod_name, namespace)
print(f"Run command for pod {pod_name} in namespace {namespace}: {run_command}")
```

### Get and Set Environment Variables for a pod

```
container_environment = hd.get_container_environment(container_id)
hd.set_container_environment(container_id, environment)
``` 

### Get and Set Volumes for a pod

```
container_volumes = hd.get_container_volumes(container_id)
hd.set_container_volumes(container_id, volumes)
```
### Example code
This example runs 4 instances of the  "Getting Started" pod

```
from shiphelm.helm import helm

hd = helm() # create an instance of helm
container_list = hd.get_running_containers() # call the method on the instance
print(container_list)
w=0

print("Preparing new server...")
while w<3:
    hd.run_container(image="ollyw123/helloworld", detach=1)
    w=w+1

print("Your server is up and ready for connection!")
```

## Dynamic engine selection
You may have noticed that the syntax for controling both Docker and Kubernetes are identical, the way the code you write for ShipHelm is run depends on the engine you selected last.

In the last example we used the follwing code to initilise ShipHelm, create an alias, and select a pod engine:

```
from shiphelm.helm import helm

hd = helm.helm() # create an instance of helm

helm.set_engine_manual("kubernetes")
```

f you want your cod to be able to use either engine that it detects locally you can use the following code instead:

```
from shiphelm.helm import helm

hd = helm.helm() # create an instance of helm

helm.set_engine_auto()
```

## Remote engines via GUI

To use remote engines you can use the following the examples above to connect programatically or use the below code to open a GUI configuration wizard:

```
from shiphelm.helm import helm

hd = helm.helm() # create an instance of helm

helm.remote_popup()
```

# Contributing

If you would like to contribute to SkiffUI, please feel free to open a pull request or issue on the [GitHub repository](https://github.com/Gameplex-Software/SkiffUI).

<script src="https://giscus.app/client.js"
        data-repo="Gameplex-Software/ShipHelm"
        data-repo-id="R_kgDOJGgWLg"
        data-category="General"
        data-category-id="DIC_kwDOJGgWLs4CVv98"
        data-mapping="pathname"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="bottom"
        data-theme="light"
        data-lang="en"
        data-loading="lazy"
        crossorigin="anonymous"
        async>
</script>
