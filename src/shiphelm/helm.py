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
kubeclient =  client

class engine:

    @staticmethod
    def set_engine_auto():
        try:
            try:
                return  kubeclient.CoreV1Api()
                print("Found Kubernetes engine on local system using Kubernetes container engine")
                engine = "kubernetes"
            except:
                return  docker.from_env()
                print("Found Docker engine on local system using Kubernetes container engine")
                enigne = "docker"
        except Exception as e:
            print("[Error] Could not locate kubernetes or docker locally, this could be sue to the current user permissions or an incompatible engine. The error is as follows:", e)

    def set_engine_manual(engine_select):
        if engine_select == "docker":
            try:
                return  docker.from_env()
                engine = "docker"
            except Exception as e:
                print("Error connecting to Docker daemon this could be sue to the current user permissions or an incompatible engine. The error is as follows:", e)
        elif engine_select == "kubernetes":
            try:
                return  kubeclient.CoreV1Api()
                engine = "docker"
            except Exception as e:
                print("Error connecting to Kubernetes daemon this could be sue to the current user permissions or an incompatible engine. The error is as follows:", e)
        else:
            print("Invalid engine", engine, ". Supported options are 'docker' or 'kubernetes'")

    def __init__(remote_address, remote_is_TLS):
        client = set_engine_auto()

    if engine == "docker":

    if engine == "kubernetes":