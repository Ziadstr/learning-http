# Use the official Python image from Docker Hub as a base image.
FROM python:3.8

# Set the working directory in the container.
WORKDIR /app

# Copy the requirements file into the container and install dependencies.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code into the container.
COPY . .

# Expose the port on which the Flask application will run.
EXPOSE 5000

# Start the Flask application when the container is run.
CMD ["python", "app.py"]
