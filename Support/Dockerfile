FROM python:3.9.0
WORKDIR /code
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#RUN apk update \
#    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
COPY . .
RUN pip install -r ./requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


