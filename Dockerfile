FROM python:3.12-slim

WORKDIR /app

# Copy the project files
COPY pyproject.toml poetry.lock /app/

# Install Poetry and dependencies
RUN pip install poetry && poetry install --no-dev

# Copy application and model files
COPY app.py app.py
COPY california_housing_pipeline.pkl california_housing_pipeline.pkl

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

EXPOSE 5000

# Use Poetry to run the app with Python
CMD ["poetry", "run", "python", "app.py"]