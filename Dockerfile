FROM python:3.10.0

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/

RUN pip install requests
RUN pip install beautifulsoup4
RUN pip install lxml

#python -m pip install requests

EXPOSE 80

COPY . .

CMD ["python", "parser.py"]
