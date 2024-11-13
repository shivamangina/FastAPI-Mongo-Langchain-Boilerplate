# ECom-FastAPI



### Setup instructions with conda

clone repo and run these commands, make sure you have mini-conda or conda installed

create a virtual environment

```
conda create --name python-backend --file requirements.txt

or

#if other env
pip install -r requirements.txt
```

activate the environment

```
conda activate python-backend
```

Exporting requirements

```
conda list -e > requirements.txt
pip3 freeze > requirements.txt
```

### Run the development server

```
python3 main.py --env dev --debug
```



### Docs

```
http://127.0.0.1:8000/docs
```

### health check

```
curl -X GET http://127.0.0.1:8000/health
```

### Deployment

```
python3 main.py --env prod
```






Build A Fast API Server That Has Multiple API.
Add environment variables and configuration


[] Database Models
[] Collections - Users

[] Add Lint
[] Login - Authenticated with JWT

[] Calls external Apis



[] Add Docker File
[] Add Docker Compose

Langchain



langchain
https://python.langchain.com/docs


