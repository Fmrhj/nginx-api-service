# API Service Template 

This is a template Flask API which can be extended to a more complex service. It includes a basic configuration of the wsgi [gunicorn](https://gunicorn.org/). It provides:

```bash
# api folder structure
+-- api
 -- Dockerfile
 -- requirements.txt
 -- gunicorn.conf.py
 -- start_api_service.sh
 -- .dockerignore
```

- `Dockerfile`: builds the Flask API container. It will be built according to the `docker-compose`
- `requirements.txt`: produced with `pip freeze > requirements.txt` or `pipreqs $(path)`
> Note: Be careful while generating the `requirements.txt` file with `pipreqs ` since it loads only imported Python modules.
- `gunicorn.conf.py`: configuration file for gunicorn server 
- `start_api_service.sh`: wrapper bash script that calls the gunicorn server with the above configuration

