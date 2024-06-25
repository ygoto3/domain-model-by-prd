FROM python:3.12-slim-bookworm

WORKDIR /app

RUN apt update && apt upgrade \
  && apt install -y curl \
  && pip install poetry \
  && poetry config virtualenvs.create false

COPY . /app/
RUN poetry install

EXPOSE 80

CMD ["uvicorn", "app.api:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]

