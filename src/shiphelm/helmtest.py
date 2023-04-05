from shiphelm import helm

helm = helm.helm

helm.set_engine_auto()
#helm.set_engine_manual("docker")
helm.get_helm_client()
print(helm.get_running_containers())
print(helm.get_running_containers())