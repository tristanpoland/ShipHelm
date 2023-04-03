from shiphelm.helm import engine

engine = engine.__init__()
engine.set_engine_manual("docker")
print(engine.get_running_containers())