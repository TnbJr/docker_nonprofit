start-dev:
	docker-compose up

stop-compose:
	@eval docker stop $(docker ps -a -q)
	docker-compose down

ssh-nginx:
	docker exec -it nginx_server bash

ssh-web:
	docker exec -it django_web bash

ssh-db:
	docker exec -it charity_db bash

build-dev:
	docker-compose build --no-cache

build-no-cache:
	docker-compose build --no-cache

logs:
	docker-compose logs -f
	
show-env:
	docker exec web env
