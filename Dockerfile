FROM python:3.9-slim

WORKDIR /llama-terminal-completion
COPY . ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y \
    wget \
    make \
    git \
    build-essential \  
 && rm -rf /var/lib/apt/lists/*

RUN yes | ./configure_llama_linux.sh

ENTRYPOINT ["python", "./watsonLlama.py"]
