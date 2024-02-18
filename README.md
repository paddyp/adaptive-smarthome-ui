# adaptive-smarthome-ui
This is a Repository for the Masterthesis 

# Requirements

- Docker and Docker-Compose 
    - for Mac Docker Desktop is needed

Tested on Mac M1, 2020 with Sonoma 14.1.1 and Docker for Mac in version XXX 

# Setup 

Execute ```docker-compose``` command on root 

``` bash
docker-compose up -d 
```

This will setup 5 Docker-Container and your Terminal should look like this: 

```
NAME                IMAGE                                     COMMAND                  SERVICE             CREATED             STATUS              PORTS
angular_admin       adaptive-smarthome-ui-angular_admin       "sh -c /app/init.sh"     angular_admin       27 hours ago        Up X hours         0/tcp, 0.0.0.0:4200->4200/tcp
angular_smarthome   adaptive-smarthome-ui-angular_smarthome   "sh -c /app/init.sh"     angular_smarthome   27 hours ago        Up X hours         0.0.0.0:4201->4200/tcp
angular_user        adaptive-smarthome-ui-angular_user        "sh -c /app/init.sh"     angular_user        27 hours ago        Up X hours         0.0.0.0:4202->4200/tcp
fastapi             adaptive-smarthome-ui-fastapi             "uvicorn main:app --…"   fastapi             27 hours ago        Up X hours         80/tcp, 0.0.0.0:8000->8000/tcp
mariadb             mariadb                                   "docker-entrypoint.s…"   mariadb             2 days ago          Up X hours         0.0.0.0:3306->3306/tcp
```

# Linklist 
### Frontend links
- Adminpanel: http://localhost:4200
- Smarthome: http://localhost:4201
- User View: http://localhost:4202
### Fasapi 

- Fastapi Websocket: ws://localhost:8000/ws
- Fastapi REST URL: http://localhost:8000 (it's not necessary)

### Mariadb 

The MariaDB Database is available at Port 3306 

# Troubleshooting 
1. Make sure, that no other Container are running. 
```bash 
docker stop $(docker ps -q) #kill all running docker Container  
```
2. Make sure no other Database is listen on Port `3306`
3. Check docker logs with the command `docker-compose logs -f`
