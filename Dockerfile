FROM python:3.11-slim as builder

WORKDIR /suchef_bot

RUN pip install --no-cache-dir uv && \
    uv venv -p python3.11 /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY pyproject.toml requirements.txt ./

RUN uv pip install --no-cache -r requirements.txt

FROM python:3.11-slim

WORKDIR /suchef_bot

COPY --from=builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1

COPY . .

CMD alembic upgrade head && python main.py