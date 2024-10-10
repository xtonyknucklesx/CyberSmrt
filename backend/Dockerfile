# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the environment variable for the default environment (can be overridden)
ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}

# If in production, run database migrations or other necessary setup
RUN if [ "${NODE_ENV}" = "production" ]; then \
        echo "Running production setup..."; \
    fi

# Expose port 8000 for the FastAPI server
EXPOSE 8000

# Command to run the FastAPI app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]