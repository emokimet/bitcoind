TAG ?= latest
IMAGE_NAME = boris/bitcoin-prometheus

.PHONY: build build-arm push login

build:
	docker build -t $(IMAGE_NAME):$(TAG) -f Dockerfile .

build-arm:
	docker buildx build --platform linux/arm64 --load --pull \
		-t $(IMAGE_NAME):$(TAG) -f Dockerfile .

