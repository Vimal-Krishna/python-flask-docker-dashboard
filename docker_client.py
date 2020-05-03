import docker

class Container:
    def __init__(self, name, status, image, ip, gateway):
        self.name = name
        self.status = status
        self.image = image
        self.ip = ip        
        self.gateway = gateway
        pass    

def get_containers():
    client = docker.APIClient(base_url="tcp://192.168.99.1:2375")
    d_containers = client.containers()
    containers = []
    for d_container in d_containers:
        inspect = client.inspect_container(d_container)
        name = inspect['Name']
        status = inspect['State']['Status']
        image = inspect['Config']['Image']
        ip = inspect['NetworkSettings']['Networks']['bridge']['IPAddress']
        gateway = inspect['NetworkSettings']['Networks']['bridge']['Gateway']
        cntr = Container(name, status, image, ip, gateway)
        containers.append(cntr)
    return containers