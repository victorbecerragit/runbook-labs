.PHONY: help list-labs setup validate validate-notebooks validate-devcontainers tree clean

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'

list-labs: ## List all available lab domains
	@echo "Available Labs:"
	@ls -1 labs/

setup: ## Install root dependencies
	python3 -m pip install -r shared/python/requirements.txt

validate: validate-devcontainers validate-notebooks ## Validate the repository structure
	@echo "Repository structure is valid."

validate-notebooks: ## Check if notebooks exist in each lab
	@for lab in labs/*; do \
		if [ ! -d "$$lab/notebooks" ]; then echo "$$lab is missing notebooks dir!"; exit 1; fi; \
		count=$$(ls -1 "$$lab/notebooks/"*.ipynb 2>/dev/null | wc -l); \
		if [ $$count -eq 0 ]; then echo "Warning: $$lab has no notebooks."; fi; \
	done
	@echo "Notebook base structure validated."

validate-devcontainers: ## Check for presence of required devcontainers
	@for dc in base rag bedrock langchain pytorch-rag; do \
		if [ ! -f ".devcontainer/$$dc/devcontainer.json" ]; then echo "Missing devcontainer: $$dc"; exit 1; fi; \
	done
	@echo "Devcontainers validated."

tree: ## Print a simplified project tree
	tree -L 4 -I '__pycache__|outputs|.ipynb_checkpoints|data'

clean: ## Remove generated caches
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
	@echo "Cleanup complete."
