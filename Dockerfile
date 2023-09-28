FROM python:3.11.5-slim
RUN mkdir /app
COPY requirements.txt /app
RUN pip3 install -r /app/requirements.txt --no-cache-dir
COPY journal/ /app
WORKDIR /app
CMD ["gunicorn", "journal.wsgi:application", "--bind", "0:8000" ] 