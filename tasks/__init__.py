import os

from invoke import task, Collection

from . import test, dc, kube


collections = [test, dc, kube]

ns = Collection()
for c in collections:
    ns.add_collection(c)

ns.configure(dict(
    project='kamailio',
    repo='docker-kamailio',
    pwd=os.getcwd(),
    docker=dict(
        user=os.getenv('DOCKER_USER'),
        org=os.getenv('DOCKER_ORG', os.getenv('DOCKER_USER', 'telephoneorg')),
        name='kazoo',
        tag='%s/%s:latest' % (
            os.getenv('DOCKER_ORG', os.getenv('DOCKER_USER', 'telephoneorg')), 'kamailio'
        ),
        services=['kamailio'],
        shell='bash'
    ),
    kube=dict(
        environment='testing'
    )
))
