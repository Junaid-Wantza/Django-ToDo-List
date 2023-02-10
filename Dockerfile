# Use an official Python runtime as the base image
FROM python:3.10.9

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Install the application's dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app/

# Set the environment variable for the Django settings module
ENV DJANGO_SETTINGS_MODULE todo_list.settings

# Expose port 80
EXPOSE 80

# Run the command to start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
