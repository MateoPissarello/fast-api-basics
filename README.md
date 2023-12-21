# Installation
```
pip intall -r requirements.txt
```



## Run APP
- uvicorn (file name): (app name) --port (port number)
    Example
    > uvicorn main:app --port 8001
### To not run it with commands add this to yout file
```
 if __name__ == "__(file name)__":
    uvicorn.run("(file_name):(app name)", port=(port number), reload= (True or False))
```
- After that just run the file
- `reload` is form enabling hot changes without having con run the server again

## Alembic Commands
```
alembic init migrations
```
```
alembic revision --autogenerate -m "(message)"
```
```
alembic upgrade heads
```
## Check Documentation
Fast API Integrates SwaggerUI by default , to check it go to {uvicorn_running_url}/docs