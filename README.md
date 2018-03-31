# Workflow scheduling optimizing budget and time in cloud computing

This repository is the one used for the project Workflow scheduling optimizing budget and time in cloud computing.

## How to use it

1. **Install Graph_tool**. This projects uses [graph_tool](https://graph-tool.skewed.de/) a module for manipulation of graphs implemented with C++. This is why we need to install a Docker Image with its dependencies, find the instructions [here](https://git.skewed.de/count0/graph-tool/wikis/installation-instructions#installing-using-docker).*

2. Run the Docker image connecting this repository folder to a folder inside the image:
```
docker run -v <path-to-repo>:/home/user -u root -ti tiagopeixoto/graph-tool bash
```
3. Navigate to the specified folder and then install the dependencies:
```
apt-get install python-pip
pip install -r requirements.txt
```
4. Run the project with:
```
python main.py
```



* Note: Native installations can be made, but it's easier to setup a Docker image.
