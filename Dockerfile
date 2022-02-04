# For more information, please refer to https://aka.ms/vscode-docker-python



FROM python:3.8



# Keeps Python from generating .pyc files in the container

ENV PYTHONDONTWRITEBYTECODE=1



# Turns off buffering for easier container logging

ENV PYTHONUNBUFFERED=1



# Install pip requirements

RUN python -m pip install pandas



RUN mkdir -p /jmeter_generator

WORKDIR /jmeter_generator

COPY . /jmeter_generator



# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug

CMD ["python", "script.py"] ;

