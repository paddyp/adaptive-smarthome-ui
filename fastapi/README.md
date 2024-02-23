# Fastapi 

This is the websocket and Persistance Controller Based on FastAPI (https://fastapi.tiangolo.com/)

# Migrations 
To create and migrate the Models SQLAlchemie and alembic is used 

A tutorial based on FastAPI can be found at https://fastapi.tiangolo.com/tutorial/sql-databases/#__tabbed_2_1

### create Migration 
```bash 
# inside the container 
alembic revision --autogenerate -m 'name_of_migration'

# outside of the container 
docker-compose exec fastapi alembic revision --autogenerate -m 'name_of_migration'
```

### execute Migration 

```bash 
# inside the container 
alembic alembic upgrade head

# outside of the container 
docker-compose exec fastapi alembic alembic upgrade head
```