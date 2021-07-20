FROM ubuntu:latest

ARG PYTHON_VERSION=3.7

ADD . /CABFARE_PREDICTION

WORKDIR /CABFARE_PREDICTION

# install miniconda and python
RUN curl -o ~/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh  && \
    chmod +x ~/miniconda.sh && \
    ~/miniconda.sh -b -p /home/containeruser/conda && \
    rm ~/miniconda.sh && \
    /home/containeruser/conda/bin/conda clean -ya && \
    /home/containeruser/conda/bin/conda install -y python=$PYTHON_VERSION 

COPY requirements.txt 
# add conda to path
ENV PATH /home/containeruser/conda/bin:$PATH

RUN pip install -r requirements.txt