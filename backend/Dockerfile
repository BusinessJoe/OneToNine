FROM python:3.11

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 8000

# Copies local directory ./app into container's /code directory.
# Not actually needed because the docker-compose file does the same,
# but having this here allows the dockerfile to be functional on its own
COPY ./app .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

# If running behind a load balancer like Nginx, uncomment next line
# CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
