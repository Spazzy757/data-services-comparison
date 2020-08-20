# Data Services Comparisons

## Comparison Matrix

Coming Soon

## Local Setup
The Local Setup is used as the the baseline, its a postgres running in docker on your local machine.

### To setup

Setup your python environment (just a note Dataflow from google only supports Python 3.5)

```bash
pyenv virtualenv -f 3.5.9 venv
pyenv activate venv

pip install -r requirements.txt
```



Start a Postgres instance
```bash
docker-compose -f docker/docker-compose.yaml up -d
```
once up and running you can run:

```bash
./environments/local/run.sh
```
this will run the pipeline twice, once with new data and once to update the existing data, 

you should get output as such:
```log
First Run
#############################################
...
INFO:root:Run Time => 0:00:53.553058
#############################################
Second Run With Updates
#############################################
...
INFO:root:Run Time => 0:00:51.237524
```

# Google Cloud Setup
Requires a Google Cloud Subscription


# Azure Setup
# AWS Setup
