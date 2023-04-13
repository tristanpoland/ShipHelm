# ----------------------------------------------------------------------------
# ShipHelm Copyright 2020-2023 by Gameplex Software and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------
import docker



class helmswarm:
    def __init__(self, remote_address=None, remote_is_TLS=None):
        try:
            except:
            helmswarm.client = docker.DockerClient(base_url=remote_address, tls=remote_is_TLS)

    @staticmethod
    def get_running_containers():
        return helmswarm.client.services.list()

    @staticmethod
    def get_container_stats(service_id):
        service = helmswarm.client.services.get(service_id)
        stats = service.stats()
        return stats
    
    @staticmethod
    def get_containerports(service_id):
        service = helmswarm.client.services.get(service_id)
        ports = service.attrs['Endpoint']['Ports']
        return ports

    @staticmethod
    def search_containers(name):
        return helmswarm.client.services.list(filters={"name": name})
    
    @staticmethod
    def change_container_ports(service_id, ports):
        service = helmswarm.client.services.get(service_id)
        service.update(EndpointSpec={'Ports': ports})

    @staticmethod
    def rename_container(service_id, new_name):
        service = helmswarm.client.services.get(service_id)
        service.update(name=new_name)

    @staticmethod
    def add_container_to_network(service_id, network_name):
        network = helmswarm.client.networks.get(network_name)
        service = helmswarm.client.services.get(service_id)
        network.connect(service)

    @staticmethod
    def remove_container_from_network(service_id, network_name):
        network = helmswarm.client.networks.get(network_name)
        service = helmswarm.client.services.get(service_id)
        network.disconnect(service)

    @staticmethod
    def create_network(network_name):
        helmswarm.client.networks.create(network_name)

    @staticmethod
    def delete_network(network_name):
        network = helmswarm.client.networks.get(network_name)
        network.remove()

    @staticmethod
    def run_container(image, command=None, detach=False, ports=None, environment=None, volumes=None):
        container = helmswarm.client.containers.run(
            image=image,
            command=command,
            detach=detach,
            ports=ports,
            environment=environment,
            volumes=volumes
        )
        return container

    @staticmethod
    def get_container_environment(container_id):
        container = helmswarm.client.containers.get(container_id)
        environment = container.attrs['Config']['Env']
        return environment

    @staticmethod
    def set_container_environment(container_id, environment):
        container = helmswarm.client.containers.get(container_id)
        container.reload()
        container.update(env=environment)

    @staticmethod
    def get_container_volumes(container_id):
        container = helmswarm.client.containers.get(container_id)
        volumes = container.attrs['HostConfig']['Binds']
        return volumes

    @staticmethod
    def set_container_volumes(container_id, volumes):
        container = helmswarm.client.containers.get(container_id)
        container.reload()
        container.update(binds=volumes)