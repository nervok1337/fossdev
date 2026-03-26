.PHONY: install typecheck run check-requirements clean format lint checkq

check: typecheck check-requirements lint

.venv:
	python -m venv .venv

install: .venv
	.venv/bin/pip install -r requirements.txt

typecheck: .venv
	.venv/bin/mypy src

run: .venv
	.venv/bin/python src/app.py

check-requirements:
	bash check_req.sh

format: .venv
	.venv/bin/black src

lint: .venv
	.venv/bin/black --check src

clean:
	rm -rf .venv
