.PHONY: build run stop check help
.DEFAULT_GOAL := help

build: ## Build bitcoin image
	docker build -t boris/bitcoin:22.0 -f Dockerfile .

run: ## Run the container exposing ports tcp:9332 and tcp:9333
	docker run --name bitcoin-22-0 -d -p 9332:9332 -p 9333:9333 boris/bitcoin:22.0

stop: ## Stop the docker container
	docker stop bitcoin-22-0

check: ## Run a security check using grype
	grype boris/bitcoin:22.0

help: ## Print this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
