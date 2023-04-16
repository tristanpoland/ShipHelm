# Copyright 2016 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Reads the list of available API versions and prints them. Similar to running
`kubectl api-versions`.
"""

from kubernetes import client, config


def main():

    # it works only if this script is run by K8s as a POD
    config.load_kube_config()
    #config.load_incluster_config(client_configuration="/etc/rancher/k3s/k3s.yaml")

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" %
              (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config()

    print("Supported APIs (* is preferred version):")
    print("%-40s %s" %
          ("core", ",".join(client.CoreApi().get_api_versions().versions)))
    for api in client.ApisApi().get_api_versions().groups:
        versions = []
        for v in api.versions:
            name = ""
            if v.version == api.preferred_version.version and len(
                    api.versions) > 1:
                name += "*"
            name += v.version
            versions.append(name)
        print("%-40s %s" % (api.name, ",".join(versions)))


if __name__ == '__main__':
    main()
