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
import docker, os
from kubernetes import client, config


class engine:
    @staticmethod
    def set_engine_auto():
        try:
            try:
                client = client()
                print("Found Kubernetes engine on local system using Kubernetes container engine")
                engine = "kubernetes"
            except:
                client = client = docker.from_env()
                print("Found Docker engine on local system using Kubernetes container engine")
                enigne = "docker"
        except Exception as e:
            print("[Error] Could not locate kubernetes or docker locally, this could be sue to the current user permissions or an incompatible engine. The error is as follows:", e)

    def set_engine_manual(engine):
        if engine == "docker":
            try:
                client = client = docker.from_env()
            except Exception as e:
                print("Error connecting to docker daemon this could be sue to the current user permissions or an incompatible engine. The error is as follows:", e)
        elif engine == "kubernetes":
            try:
                client = client = docker.from_env()
            except Exception as e:
                print("Error connecting to docker daemon this could be sue to the current user permissions or an incompatible engine. The error is as follows:", e)
        else:
            print("Invalid engine", engine, ". Supported options are 'docker' or 'kubernetes'")

    def __init__(self, remote_address, remote_is_TLS):
        self.client = self.set_engine_auto()


    if engine == "docker":
        @staticmethod
        def get_running_containers(self):
            client = self.get_engine()
            return client.containers.list()

        @staticmethod
        def get_container_stats(self, container_id):
            client = self.get_engine()
            container = client.containers.get(container_id)
            stats = container.stats(stream=False)
            return stats

        @staticmethod
        def get_container_ports(self, container_id):
            client = self.get_engine()
            container = client.containers.get(container_id)
            ports = container.attrs['NetworkSettings']['Ports']
            return ports

        @staticmethod
        def search_containers(self, name):
            client = self.get_engine()
            return client.containers.list(filters={"name": name})

        @staticmethod
        def change_container_ports(self, container_id, ports):
            client = self.get_engine()
            container = client.containers.get(container_id)
            container.reload()
            container.ports.update(ports)

        @staticmethod
        def rename_container(self, container_id, new_name):
            client = self.get_engine()
            container = client.containers.get(container_id)
            container.rename(new_name)

        @staticmethod
        def add_container_to_network(self, container_id, network_name):
            client = self.get_engine()
            network = client.networks.get(network_name)
            container = client.containers.get(container_id)
            network.connect(container)

        @staticmethod
        def remove_container_from_network(self, container_id, network_name):
            client = self.get_engine()
            network = client.networks.get(network_name)
            container = client.containers.get(container_id)
            network.disconnect(container)

        @staticmethod
        def create_network(self, network_name):
            client = self.get_engine()
            client.networks.create(network_name)

        @staticmethod
        def delete_network(self, network_name):
            client = self.get_engine()
            network = client.networks.get(network_name)
            network.remove()

        @staticmethod
        def run_container(self, image, command=None, detach=False, ports=None, environment=None, volumes=None):
            client = self.get_engine()
            container = client.containers.run(
                image=image,
                command=command,
                detach=detach,
                ports=ports,
                environment=environment,
                volumes=volumes
            )
            return container

        @staticmethod
        def get_container_environment(self, container_id):
            client = self.get_engine()
            container = client.containers.get(container_id)
            environment = container.attrs['Config']['Env']
            return environment

        @staticmethod
        def set_container_environment(self, container_id, environment):
            client = self.get_engine()
            container = client.containers.get(container_id)
            container.reload()
            container.update(env=environment)

        @staticmethod
        def get_container_volumes(self, container_id):
            client = self.get_engine()
            container = client.containers.get(container_id)
            volumes = container.attrs['HostConfig']['Binds']
            return volumes

        @staticmethod
        def set_container_volumes(self, container_id, volumes):
            client = self.get_engine()
            container = client.containers.get(container_id)
            container.reload()
            container.update(binds=volumes)