test:
	pytest timeline/tests/

clean:
	@rm -rf .Python MANIFEST build dist venv* *.egg-info *.egg .eggs .cache
	@rm -rf .pytest_cache .coverage
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete

.PHONY: test clean
