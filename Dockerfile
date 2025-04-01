FROM python:3.13
WORKDIR /usr/local/app
COPY src .
CMD ["python3", "main.py"]