.DEFAULT_GOAL := help

PRODUCT_HOST ?= 127.0.0.1
PRODUCT_PORT ?= 8001

ORDER_HOST ?= 127.0.0.1
ORDER_PORT ?= 8002

PRODUCT_SERVICE_URL = http://$(PRODUCT_HOST):$(PRODUCT_PORT)

create-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	@echo "Createing practice"
	mkdir -p $(PRACTICE)
	cp PracticeMakefile $(PRACTICE)/Makefile

remove-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	rm -rf $(PRACTICE)

help:
	@echo "This makefile for repo-level activity"

run-servide:
	cd product_service && venv/bin/poetry run uvicorn src.app.main:app --host $(PRODUCT_HOST) --port $(PRODUCT_PORT) & \
	PRODUCT_PID=$$!; \
	sleep 2; \
	cd order_service && PRODUCT_SERVICE_URL=$(PRODUCT_SERVICE_URL) venv/bin/poetry run uvicorn src.app.main:app --host $(ORDER_HOST) --port $(ORDER_PORT); \
	kill $$PRODUCT_PID

