from docker import Client
cli = Client(base_url='http://localhost:2375')
print cli.containers()
