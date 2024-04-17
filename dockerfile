FROM python:3.11.8
LABEL Name = "Weather in Delft App"
WORKDIR /app

# setting up python
ENV PYTHONUNBUFFERED=1
RUN pip install --no-cache-dir --upgrade pip
RUN pip install requests

# setting up application 
COPY ./src/ ./
CMD [ "python", "./HoeWarmIsHetInDelft.py" ]