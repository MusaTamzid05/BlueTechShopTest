import os

def get_postgres_host():

    '''
    This is a hack a for getting the postgres server address
    in this container.The postgres server is running on
    another container and when linked with this container,
    does not runs on "0.0.0.0".So this function return
    the current address.
    '''

    postgres_container_name = os.environ["POSTGRES_CONTAINER"]

    with open("/etc/hosts") as f:
        for line in f.readlines():
            data = line.split()

            if postgres_container_name in data:
                return data[0]

    raise RuntimeError("Docker container not likned properly!!")

