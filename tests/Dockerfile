FROM python:3.9-slim

WORKDIR /app

# Install app dependencies
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt 


# Copy app files
COPY . .

# Expose port for Locust web UI
EXPOSE 8089

# Start the Locust test
CMD ["locust", "-f", "locustfile.py", "--headless", "--host", "https://default-service-2hwdmv3hoq-nw.a.run.app/"]
