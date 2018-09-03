import docker 
#print dir(docker.client)
client = docker.APIClient(base_url='tcp://192.168.56.101:2375')
#print client.version()

#li = Client(base_url='http://localhost:2375')
#cli = docker.from_env(base_url='http://192.168.56.101:2375')

#print cli.containers()
#client.inspect_container('romantic_feynman')['State']['Status']
inspect_romantic_feynman = client.inspect_container('romantic_feynman')['State']['Status']

print is_romantic_feynman

if is_romantic_feynman == 'running':
	print 'Container romantic_feynman is running! Trying to stop ...'
	client.stop('romantic_feynman')
else:
        print('Container is stopped. Sorry, but nothing to to! ') 

print 'Container romantic_feynman now have a status: ' + inspect_romantic_feynman



