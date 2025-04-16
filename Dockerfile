FROM python:3.11-slim

WORKDIR /app

COPY hivebox.py .

CMD [ "python","hivebox.py" ]