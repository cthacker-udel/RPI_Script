FROM python:3.12-slim

# Set the working directory to the `app` directory.
WORKDIR /app

# Copy over all the files to the `app` directory.
COPY . /app

# Install + Update dependencies
RUN apt-get update && apt-get install -y --no-install-recommends build-essential curl git

COPY requirements.txt .
RUN pip3 install -v --no-cache-dir -r requirements.txt && pip3 install mysql-connector-python
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

COPY . .

# Run the base CLI file.
CMD ["python", "main.py"]

