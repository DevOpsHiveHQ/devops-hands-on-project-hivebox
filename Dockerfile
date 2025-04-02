# Use an official Python base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file first (to leverage Docker caching)
COPY requirements.txt .

# Install Python dependencies
#RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install --no-cache-dir -i https://pypi.org/simple -r requirements.txt
RUN pip install --no-cache-dir -r  requirements.txt


# Copy the rest of the application code
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
