FROM python:3.9

# Avoid writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# make console not buffered by Docker
ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
 
