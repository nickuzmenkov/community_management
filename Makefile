CODE=community_management
CODE_TESTS=tests
MIN_TEST_COVERAGE=95

format:
	ruff format $(CODE) $(CODE_TESTS)

lint:
	ruff check $(CODE)

test:
	pytest --cov=$(CODE) --cov-fail-under=$(MIN_TEST_COVERAGE) $(CODE_TESTS)
