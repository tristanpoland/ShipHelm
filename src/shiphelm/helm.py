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

try:
    from . import helmdocker, helmkube
except:
    print("Error: Shiphelm cannot be run from source!")
    exit()
from kubernetes import client
from typing import TYPE_CHECKING
import docker

#Fix name conflict between docker nad kubernetes client
kubeclient = client

#Fix editor auto completes that are broken by the dynamic functions
if TYPE_CHECKING:
    from . import helmdocker, helmkube
    from helmdocker import helmdocker
    from helmdocker import *
    from helmkube import helmkube
    from helmkube import *

class helm:
    def __init__():
        helm.engine = helm.set_engine_auto()
        helm.get_helm_client()

    def set_engine_auto():
        helm.engine = None
        try:
            v1 = kubeclient.CoreV1Api()
            helm.engine = "kubernetes"
            v1.list_pod_for_all_namespaces(watch = False)
            print("Found Kubernetes engine on local system using Kubernetes container engine")
        except:
            try:
                docker.from_env()
                print("Found Docker engine on local system using Kubernetes container engine")
                helm.engine = "docker"
            except:
                pass

        if not helm.engine:
            print("[Error] Could not locate kubernetes or docker locally, this could be due to the current user permissions or an incompatible engine.")

        return helm.engine

    def set_engine_manual(engine_select):
        helm.engine = None
        if engine_select == "docker":
            try:
                docker.from_env()
                helm.engine = "docker"
            except Exception as e:
                print("Error connecting to Docker daemon this could be due to the current user permissions or an incompatible engine. The error is as follows:", e)
        elif engine_select == "kubernetes":
            try:
                kubeclient.CoreV1Api()
                helm.engine = "kubernetes"
            except Exception as e:
                print("Error connecting to Kubernetes daemon this could be due to the current user permissions or an incompatible engine. The error is as follows:", e)
        else:
            print("Invalid engine", engine_select, ". Supported options are 'docker' or 'kubernetes'")

        return helm.engine
    
    def add_methods(cls):
        methods = [m for m in dir(cls) if not m.startswith("__") and callable(getattr(cls, m))]
        print(methods)

        for method in methods:
            setattr(helm, method, getattr(cls, method))

    def get_helm_client():
        print("Selected engine for runner:", helm.engine)
        if helm.engine == "docker":
            helm.add_methods(helmdocker.helmdocker)
            return helmdocker.helmdocker()
        elif helm.engine == "kubernetes":
            helm.add_methods(helmkube.helmkube)
            return helmkube.helmkube()
