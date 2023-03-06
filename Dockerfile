# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

ENV PORT 8080
ENV HOST 0.0.0.0

EXPOSE 8080

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable

# Run app.py when the container launches
CMD ["python", "app.py"]
