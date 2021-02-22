from homi import App, Server
from homi.extend.service import reflection_service, health_service
from owner_client import notify_owner

from dog_pb2 import _DOG


app = App(
    services=[
        _DOG,
        reflection_service,
        health_service,
    ]
)

service_name = 'proto.dog'

@app.method(service_name,'CallDog')
def call_dog(**kwargs):
    dog_name = kwargs.pop('request').dogName
    print(f"{dog_name} is going to bark!")
    notify_owner(dog_name)
    return {"dogBark": f"{dog_name} is barking"}

if __name__ == '__main__':
    server = Server(app)
    server.run()