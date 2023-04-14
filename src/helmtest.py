from shiphelm.helm import helm

hd = helm()

id = "fd452e129855"
ctr_id = id

print(helm.get_running_containers())
print(helm.get_container_stats(ctr_id))
helm.rename_container(id, "hello world")
ctr_object = helm.get_container_by_id(ctr_id)
print(ctr_object)
