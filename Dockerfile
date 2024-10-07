# Use the official Python image from Docker Hub
FROM python:3.9-slim

RUN apt-get update && apt-get install -y wget gcc

RUN groupadd -r appuser && useradd -r -g appuser appuser

RUN mkdir /home/appuser && chown -R appuser:appuser /home/appuser

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Change ownership of the directory to the non-root user
RUN chown -R appuser:appuser /app


RUN wget https://github.com/bazelbuild/bazelisk/releases/download/v1.22.0/bazelisk-linux-amd64 && \
    chmod 755 bazelisk-linux-amd64 && \
    mv bazelisk-linux-amd64 /usr/bin/bazelisk

# Switch to the non-root user
USER appuser

# Install the Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt
RUN bazelisk build //:app

# Expose the port that the Flask app runs on
EXPOSE 5000

# Command to run the Flask app
# CMD ["python", "app.py"]

CMD ["bazelisk", "run", "//:app"]
