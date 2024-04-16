FROM python:3
WORKDIR /app

RUN pip install --no-cache-dir requests
COPY ./HoeWarmIsHetInDelft.py /app
COPY ./utility.py /app
CMD [ "python", "./HoeWarmIsHetInDelft.py" ]

