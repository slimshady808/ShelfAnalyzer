# Use an official Python runtime as a parent image
FROM python:3

# Set environment variables (adjust as needed)
# ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

# Create and set the working directory
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install  -r requirements.txt

# Copy the current directory contents into the container
COPY . /code/


