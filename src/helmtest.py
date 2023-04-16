from shiphelm.helm import helm

hd = helm()

id = "7dada6452d6d2f131d79e22a9274d521b915ba6b764f1dd140731195cf8a58a7"
ctr_id = id

print(helm.get_running_containers())
print(helm.get_container_stats(ctr_id))
helm.rename_container(id, "hello-there")
ctr_object = helm.get_container_by_id(ctr_id)
print(ctr_object)
