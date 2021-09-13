FROM python:3.9.0
WORKDIR /code
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
COPY . .
RUN pip install -r ./requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


