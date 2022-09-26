FROM python:3.10


RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg2 dependencies
  libpq-dev

RUN pip install --upgrade pip

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir --upgrade -r /app/src/requirements.txt

COPY start.sh /start-sh

RUN sed -i 's/\r$//g' /start-sh

RUN chmod +x /start-sh

# copy application code to WORKDIR
COPY . /app
