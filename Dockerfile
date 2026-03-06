FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 10000
EXPOSE 5005
EXPOSE 5055

CMD ["sh", "start.sh"]