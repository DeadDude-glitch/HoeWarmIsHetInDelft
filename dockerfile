FROM python:3.10
WORKDIR /app
ENV PYTHONUNBUFFERED=1

RUN pip install requests
COPY ./HoeWarmIsHetInDelft.py /app
COPY ./utility.py /app
CMD [ "python", "./HoeWarmIsHetInDelft.py" ]