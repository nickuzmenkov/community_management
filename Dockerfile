FROM python:3.11.5

RUN pip install poetry==1.5.1
COPY pyproject.toml ./
RUN poetry install

RUN pwd
COPY . ./
ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "community_management.app:app"]
