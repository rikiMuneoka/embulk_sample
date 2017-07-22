pip=$(shell which pip)
python=$(shell which python)

.PHONY: setup

setup:
	$(pip) install faker --user

create_sql:
	$(python) createSQL.py
