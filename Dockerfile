FROM python:3.6.5-alpine3.7

LABEL maintainer="kyledevinobrien1@gmail.com"

COPY requirements.txt /lisent/requirements.txt

RUN pip install -r /lisent/requirements.txt

COPY . /lisent/

WORKDIR /lisent/

RUN python -m textblob.download_corpora

EXPOSE 5000

CMD ["python", "app.py"]