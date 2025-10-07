FROM python:3.12-slim

WORKDIR /app

COPY /requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DB_USER=ai_readonly
ENV DB_PASSWORD=supersecret
ENV DB_HOST=localhost
ENV DB_PORT=5432
ENV DB_NAME=demo
ENV AGENT_LOG_FILE=agent.log

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
