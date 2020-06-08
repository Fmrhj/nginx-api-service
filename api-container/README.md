# API Service Template 

This is a template Flask API which can be extended to a more complex service. It includes a basic configuration of the wsgi [gunicorn](https://gunicorn.org/). It provides:

```bash
# api folder structure
+-- api-container
    +-- api
        +-- endpoints
            ...
        -- __init__.py
        -- api.py
    -- .dockerignore
    -- Dockerfile
    -- gunicorn.conf.py
    -- start_api_service.sh
    -- requirements.txt
    -- wsgi.py
```

## App configuration and Docker files

- `Dockerfile`: builds the Flask API container. It will be built according to the `docker-compose`
- `requirements.txt`: produced with `pip freeze > requirements.txt` or `pipreqs $(path)`
> Note: Be careful while generating the `requirements.txt` file with `pipreqs ` since it loads only imported Python modules
- `wsgi.py`: imports the application module from `api.py`. 
- `gunicorn.conf.py`: configuration file for gunicorn server 
- `start_api_service.sh`: wrapper bash script that calls the gunicorn server with the above configuration. It is also the `CMD` entry point of the Docker container


## App logic and modules

The `api` subfolder contains the application logic in the `api.py` file. Further subfolders and endpoints can be added as modules in the `endpoint` subfolder.