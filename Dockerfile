FROM python:3.7.0-alpine3.8

LABEL maintainer="kyledevinobrien1@gmail.com"

COPY requirements.txt /lisent/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r /lisent/requirements.txt

COPY . /lisent/

WORKDIR /lisent/

RUN python -m textblob.download_corpora

RUN python nltk_setup.py

EXPOSE 5000

CMD ["python", "-u", "app.py"]