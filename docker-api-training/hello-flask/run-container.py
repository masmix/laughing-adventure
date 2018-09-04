from docker import Client
cli = Client(base_url='http://172.18.0.2:2375')
cli.containers()
#client.inspect_container('romantic_feynman')['State']['Status']

