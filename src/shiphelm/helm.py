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

import helmdocker, helmkube
from kubernetes import client
from typing import TYPE_CHECKING
import docker
import tkinter as tk
from tkinter import ttk

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
    def __init__(self, engine=None):
        helm.engine = helm.set_engine_auto()
        helm.get_helm_client()

    def set_engine_auto():
        helm.engine = None
        try:
            v1 = kubeclient.CoreV1Api()
            api = v1.CoreV1Api()
            helm.engine = "kubernetes"
            namespaces = api.list_namespace().items
            print("Found Kubernetes engine on local system using Kubernetes container engine")
        except:
            pass
        if not helm.engine:
            try:
                docker.from_env()
                print("Found Docker engine on local system using Docker container engine")
                helm.engine = "docker"
            except:
                print("[Debug] No compatible engine found, prompting for remote connection")
                helm.remote_popup()
                print("Popup got engine data:", helm.engineAddress, helm.engineType)

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
    
    def remote_popup():
        # Create a popup window
        window = tk.Tk()
        window.title("Remote Address")

        # Create a label and text input field for the remote address
        tk.Label(window, text="Remote Address:").grid(row=0, column=0)
        remote_address = tk.Entry(window)
        remote_address.grid(row=0, column=1)

        # Create a label and dropdown menu for the options
        tk.Label(window, text="Options:").grid(row=1, column=0)
        options = ttk.Combobox(window, values=["Option 1", "Option 2", "Option 3"])
        options.current(0)
        options.grid(row=1, column=1)

        # Add a button to submit the inputs
        submit_button = tk.Button(window, text="Submit")
        submit_button.grid(row=2, column=1)

        # Return values
        helm.engineAddress = remote_address
        helm.engineType = options.get()

        # Start the event loop
        window.mainloop()

    def add_methods(cls):
        methods = [m for m in dir(cls) if not m.startswith("__") and callable(getattr(cls, m))]

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