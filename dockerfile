FROM python:3.11
WORKDIR /app

RUN pip install --no-cache-dir requests
ENV PYTHONUNBUFFERED=1
COPY ./HoeWarmIsHetInDelft.py /app
COPY ./utility.py /app
CMD [ "python", "./HoeWarmIsHetInDelft.py" ]