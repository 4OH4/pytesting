# base image
FROM continuumio/miniconda3

USER root

WORKDIR "/"

# load in the Conda environment.yml file
# ADD ./environment.yml /

# update the environnment
# RUN conda env update -f environment.yml


# load in the Pip requirements.txt file (assumes context is parent folder...)
ADD ./requirements.txt /

# update the environnment
RUN pip install -r requirements.txt

WORKDIR "/working"