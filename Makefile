build:
	@docker compose build

up:
	@docker compose up -d

down:
	@docker compose down

inside:
	@docker exec -it my-iris bash

iris:
	@docker exec -it my-iris irissession iris

logs:
	@docker compose logs