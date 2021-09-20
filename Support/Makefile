WEB_CONTAINER_NAME=support
WEB_SERVICE_NAME=web
DEFAULT_DB=postgres


mkm: ## make migrations
	docker exec -it ${WEB_CONTAINER_NAME} python manage.py makemigrations

m: ## migrate
	docker exec -it ${WEB_CONTAINER_NAME} python manage.py migrate

csu: ## create superuser
	docker exec -it ${WEB_CONTAINER_NAME} python manage.py createsuperuser

exec: ## exec web container
	docker exec -it ${WEB_CONTAINER_NAME} bash

exec_db: ## exec db container
	docker exec -it ${POSTGRES_CONTAINER_NAME} bash
load:
	docker exec -it ${WEB_CONTAINER_NAME} ./manage.py loaddata fixture
