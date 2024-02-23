FROM --platform=$BUILDPLATFORM tiangolo/uvicorn-gunicorn-fastapi:python3.10
RUN pip install --upgrade pip
COPY ./app /app
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
