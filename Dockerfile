#FROM demisto/python3
FROM python:3
WORKDIR /usr/src/app

COPY main.py ./
#RUN pip install --no-cache-dir -r
COPY . .
CMD [ "python", "./main.py" ]

