# Step 1: Use official Python image
FROM python:3.11

# Step 2: Set working directory inside container
WORKDIR /app

# Step 3: Copy project files into container
COPY . .

# Step 4: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose the port FastAPI will run on
EXPOSE 8000

# Step 6: Start FastAPI when container starts
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]