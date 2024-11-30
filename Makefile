DOCKER_IMAGE = "lab"

docker-build:
	docker build -t $(DOCKER_IMAGE) .

docker-run:
	docker run -p 8888:8888 --network="host" --restart always -d -t $(DOCKER_IMAGE)
