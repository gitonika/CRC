# Use an official python runtime as a parent image
FROM python:3.12-slim

#Set the working directory in the container to /app
WORKDIR /app

#Copy the current directory contents into the containter /app
COPY . /app

#Install any needed documentation specified in the requirements .txt
RUN pip install fastapi uvicorn
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
RUN pip install sqlalchemy

ENTRYPOINT fastapi run main.py

#Run the app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]