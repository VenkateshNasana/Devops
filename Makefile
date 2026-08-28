.PHONY: build run test

build:
	docker-compose build

run:
	docker-compose up -d

test:
	cd backend && python manage.py test
