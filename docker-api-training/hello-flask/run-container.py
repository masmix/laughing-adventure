from docker import Client
cli = Client(base_url='http://172.18.0.2:2375')
cli.containers()
