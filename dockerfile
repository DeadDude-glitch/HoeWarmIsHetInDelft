FROM python:3.11.8
LABEL Name = "Back In Delft Python App"
WORKDIR /app
 

# setting up python
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
COPY ./src/requirements.txt ./
RUN pip install -r ./requirements.txt

COPY ./src/HoeWarmIsHetInDelft.py ./

CMD ["python3", "HoeWarmIsHetInDelft.py"]