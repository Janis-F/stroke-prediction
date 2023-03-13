FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["locust", "--host=https://default-service-2hwdmv3hoq-nw.a.run.app", "--users=300", "--spawn-rate=5", "--headless"]

