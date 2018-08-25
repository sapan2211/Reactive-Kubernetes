FROM python:3.7-alpine3.7
COPY . /app
WORKDIR /app
RUN pip install rq
RUN pip install --upgrade setuptools
RUN pip install redis 
RUN pip install kubernetes
EXPOSE 80
CMD python ./worker.py
