FROM python:3.9.0
WORKDIR /code
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY . .
RUN apt-get update
RUN apt-get install -y libpq-dev
RUN apt-get install -y gcc
RUN apt-get install gettext -y
RUN pip install -r ./requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


