gen-docs:
	python3 ./scripts/generate_docs.py
	gendocs --config mkgendocs.yaml

mkdocs:
	make gen-docs
	mkdocs serve