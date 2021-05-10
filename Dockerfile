FROM python:3.9.0

WORKDIR /code

ENV VIRTUAL_ENV=/env
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .

RUN  pip install -r requirements.txt

COPY tflapp ./tflapp
COPY tflapp.py .

ARG TFL_KEY
ENV TFL_KEY=$TFL_KEY

ENTRYPOINT FLASK_APP=tflapp.py flask run --host=0.0.0.0
