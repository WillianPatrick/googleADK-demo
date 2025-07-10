FROM python:alpine

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src .
ENV PYTHONUNBUFFERED=1

EXPOSE 8000
# lança servidor REST do ADK
CMD ["adk", "web", "--host=0.0.0.0"]