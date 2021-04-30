TAG ?= latest
IMAGE_NAME = boris/bitcoin-prometheus

.PHONY: build push

build:
	docker buildx build --platform linux/amd64,linux/arm64 --load --pull \
		-t $(IMAGE_NAME):$(TAG) -f Dockerfile .

push:
	docker push $(IMAGE_NAME):$(TAG)
