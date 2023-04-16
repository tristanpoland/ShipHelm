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

from kubernetes import client, config

class helmkube:
    def __init__(self, remote_address = None, remote_is_TLS = None):
        try:
            helmkube.kubeclient = client
            config.load_kube_config()
            helmkube.api_client = helmkube.kubeclient.ApiClient()
            namespace = "default"  # modify as needed
        except:
            pass
            #Finish: Remote Kubernetes connection

    def get_running_containers(self):
        api_instance = helmkube.kubeclient.CoreV1Api(helmkube.api_client)
        pods = api_instance.list_pod_for_all_namespaces(watch=False)
        containers = []
        for pod in pods.items:
            for container in pod.spec.containers:
                containers.append(container)
        return containers

    def get_container_by_id(self, container_id):
        return self.get_container_by_id(container_id)

    def get_container_stats(self, container_id):
        api_instance = helmkube.kubeclient.CoreV1Api(helmkube.api_client)
        namespace = "default"  # modify as needed
        pod_name = container_id  # use container ID as pod name
        container_name = container_id  # use container ID as container name
        container_stats = api_instance.read_namespaced_pod_container_status(
            name=pod_name,
            namespace=namespace,
            container=container_name
        )
        return container_stats

    def get_container_ports(self, container_id):
        api_instance = helmkube.kubeclient.CoreV1Api(helmkube.api_client)
        namespace = "default"  # modify as needed
        pod_name = container_id  # use container ID as pod name
        container_name = container_id  # use container ID as container name
        container = api_instance.read_namespaced_pod(
            name=pod_name,
            namespace=namespace
        )
        ports = container.spec.containers[0].ports
        return ports

    def search_containers(self, name):
        api_instance = helmkube.kubeclient.CoreV1Api(helmkube.api_client)
        namespace = "default"  # modify as needed
        label_selector = f"name={name}"
        pods = api_instance.list_namespaced_pod(
            namespace=namespace,
            label_selector=label_selector
        )
        containers = []
        for pod in pods.items:
            for container in pod.spec.containers:
                containers.append(container)
        return containers

    def change_container_ports(self, container_id, ports):
        api_instance = helmkube.kubeclient.CoreV1Api(helmkube.api_client)
        namespace = "default"  # modify as needed
        pod_name = container_id  # use container ID as pod name
        container_name = container_id  # use container ID as container name
        container = api_instance.read_namespaced_pod(
            name=pod_name,
            namespace=namespace
        )
        container.spec.containers[0].ports = ports
        api_instance.patch_namespaced_pod(
            name=pod_name,
            namespace=namespace,
            body=container
        )

    def rename_container(self, container_id, new_name):
        api_instance = helmkube.kubeclient.CoreV1Api(helmkube.api_client)
        namespace = "default"  # modify as needed
        pod_name = container_id  # use container ID as pod name
        container_name = container_id  # use container ID as container name
        container = api_instance.read_namespaced_pod(
            name=pod_name,
            namespace=namespace
        )
        container.metadata.name = new_name
        api_instance.replace_namespaced_pod(
            name=pod_name,
            namespace=namespace,
            body=container
        )

    @staticmethod
    def add_container_to_network(self, container_id, network_name):
        # Kubernetes has a different networking model, so this method is not applicable
        pass

    @staticmethod
    def remove_container_from_network(self, container_id, network_name):
        # Kubernetes has a different networking model, so this method is not applicable
        pass

    @staticmethod
    def create_service(self, service_name, app_name, container_port):
        namespace = "default"  # modify as needed
        v1 = helmkube.kubeclient.CoreV1Api()
        service_manifest = {
            "apiVersion": "v1",
            "kind": "Service",
            "metadata": {
                "name": service_name,
            },
            "spec": {
                "selector": {
                    "app": app_name,
                },
                "ports": [
                    {
                        "name": "http",
                        "port": 80,
                        "targetPort": container_port,
                    }
                ],
                "type": "ClusterIP"
            }
        }
        v1.create_namespaced_service(namespace, service_manifest)

    @staticmethod
    def set_container_volumes(self, container_name, volumes):
        namespace = "default"  # modify as needed
        v1 = helmkube.kubeclient.CoreV1Api()
        container = v1.read_namespaced_pod(container_name, namespace)
        container.spec.volumes = volumes
        v1.replace_namespaced_pod(container_name, namespace, container)