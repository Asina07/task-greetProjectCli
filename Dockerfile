# # Use official Python image
# FROM python:3.10

# # Set working directory inside container
# WORKDIR /app

# # Copy all project files
# COPY . .

# # Install dependencies
# RUN pip install -r requirements.txt

# EXPOSE 5000

# # Default command to run your Python script
# CMD ["python", "greet.py"]
FROM python:3.10

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "app.py"]
