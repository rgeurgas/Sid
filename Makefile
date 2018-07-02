DOCKER := docker-compose

all:
	$(DOCKER) up

migrations:
	$(DOCKER) run web python3 manage.py makemigrations
	$(DOCKER) run web python3 manage.py migrate

start:
	$(DOCKER) build
	sudo chown -R $(USER):$(USER) .
	make all

clear:
	$(DOCKER) stop
	$(DOCKER) rm
	$(DOCKER) up -d --force-recreate
