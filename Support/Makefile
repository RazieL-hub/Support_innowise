POSTGRES_CONTAINER_NAME=podpisby2_postgres
WEB_CONTAINER_NAME=support
WEB_SERVICE_NAME=web
DEFAULT_DB=postgres


mkm: ## make migrations
	docker exec -it ${WEB_CONTAINER_NAME} python manage.py makemigrations

m: ## migrate
	docker exec -it ${WEB_CONTAINER_NAME} python manage.py migrate

csu: ## create superuser
	docker exec -it ${WEB_CONTAINER_NAME} python manage.py createsuperuser

cm: ## compile messages translations
	docker exec -it ${WEB_CONTAINER_NAME} python manage.py compilemessages

update: ## git pull and back web restart
	git pull
	docker-compose -f docker-compose.stage.yml restart

cs:  ## collect static
	docker exec -it ${WEB_CONTAINER_NAME} python manage.py collectstatic

h: ## help dialog
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

exec: ## exec web container
	docker exec -it ${WEB_CONTAINER_NAME} bash

exec_db: ## exec db container
	docker exec -it ${POSTGRES_CONTAINER_NAME} bash

reminder: ## sending reminder letters to sign documents
	docker exec -it ${WEB_CONTAINER_NAME} python manage.py reminder

agent_all: ## set can_use_agent=True of User model
	docker exec -it ${WEB_CONTAINER_NAME} python manage.py agent_all
load:
	docker exec -it ${WEB_CONTAINER_NAME} ./manage.py loaddata test1
