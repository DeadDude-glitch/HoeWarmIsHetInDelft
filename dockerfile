FROM python:3.10
WORKDIR /app

RUN pip install requests
ENV PYTHONUNBUFFERED=1
COPY ./HoeWarmIsHetInDelft.py /app
COPY ./utility.py /app
CMD [ "python", "./HoeWarmIsHetInDelft.py" ]