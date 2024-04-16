FROM python:3.11.8

LABEL Name = "Weather in Delft App"

WORKDIR /app
ENV PYTHONUNBUFFERED=1

RUN pip install requests
COPY ./src/ .
CMD [ "python", "./HoeWarmIsHetInDelft.py" ]