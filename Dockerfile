FROM python:3.12.2-slim-bullseye

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

RUN apt-get update && apt-get install -y curl

COPY . .

ENV FLASK_APP=__init__.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
