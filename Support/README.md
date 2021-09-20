Z49-TMS


Django rest framework api

This is a django-rest-framework support application

Библиотеки, которые используются:

Django, django-rest-framework, simpleJWT, django-filters, celery, redis, Docker, Docker-Compose


Django-rest-framework support application включает в себя:
- Регистрация, логин, логаут
- Профиль пользователя:
Возможность изменния и сохранения всех личных данных.
Возможность просмотра чужого профиля и его тикетов.

Модель тикета (CRUD)

1) Создание тикета (Create)

2) Чтение тикета (Read)

3) Редактирование тикета (Update)

4) Удаление тикета (Delete)

Модель комментариев

1) создание комментария
2) добавление комментария к нужному тикету.

Как запустить проект у себя?

1 - git clone https://github.com/RazieL-hub/support_ticket

2 - запросить у владельца проекта .env файл

3 - .env файл положить в папку проекта Support(mac) или Support/Support(Linux)

4 - выбрать интерпретатор из Support --> docker-compose.yml  Service Web

5 - Запустить проект

6 - Находясь в директории, где лежит Makefile прописать:
make mkm --> make m  --> make load


