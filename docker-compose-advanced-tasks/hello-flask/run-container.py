#import docker
#client = docker.from_env()
#container = client.containers.run("bfirsh/reticulate-splines", detach=True)
#print container.id
import docker
client = docker.from_env()
print dir(client.images)
#for image in dir(client.images):
#  print image.id
#container = client.containers.get('f1064a8a4c82')
#print container.logs()


