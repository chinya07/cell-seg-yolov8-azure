# cell-segmentation-yolov8

## Workflows

1. constants
2. entity
3. components
4. pipelines
5. app.py


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/chinya07/instance-segmentation-yolov8-aws
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cell python=3.8 -y
```

```bash
conda activate cell
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


# AZURE-CICD-Deployment-with-Github-Actions

## Save pass:

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
## Run from terminal:

docker build -t <container_name>.azurecr.io/cell:latest .

docker login <container_name>.azurecr.io

docker push <container_name>.azurecr.io/cell:latest


## Deployment Steps:

1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure 
4. Pull the Docker image from the container registry to Web App server and run 


