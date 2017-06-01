# Use an official Python runtime as a base image
FROM resin/raspberry-pi3-python:3.6-slim

# Copy the current directory contents into the container at /app
ADD . /code

# Set the working directory to /code
WORKDIR /code

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD ["python", "app.py"]