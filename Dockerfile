FROM python:3.8

ADD nodo1.py .

COPY requirements.txt /requirements.txt
COPY . /.
RUN pip3 install -r requirements.txt

CMD ["python","./nodo1.py"]

