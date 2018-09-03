from docker import Client
cli = Client(base_url='http://localhost:2375')
print cli.containers()
#client.inspect_container('romantic_feynman')['State']['Status']
is_romantic_feynman = cli.inspect_container('romantic_feynman')['State']['Status']
print is_romantic_feynman
