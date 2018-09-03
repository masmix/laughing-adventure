import docker 
#li = Client(base_url='http://localhost:2375')
cli = docker.from_env(base_url='http://192.168.56.101:2375')

print cli.containers()
#client.inspect_container('romantic_feynman')['State']['Status']
is_romantic_feynman = cli.inspect_container('romantic_feynman')['State']['Status']
print is_romantic_feynman
