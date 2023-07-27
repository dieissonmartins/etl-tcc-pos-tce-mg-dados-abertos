FROM python:3.9

LABEL maintainer="Dieisson <dieisson.martins.santos@gmail.com>"

EXPOSE 5000

ADD . .

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD python main.py