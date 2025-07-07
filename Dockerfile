FROM nvidia/cuda:12.2.0-cudnn8-runtime-ubuntu22.04

# Install Python 3.10, pip, and Git
RUN apt-get update && apt-get install -y \
    python3.10 python3-pip git && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN python3.10 -m pip install --upgrade pip

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN python3.10 -m pip install -r requirements.txt

# Copy the rest of the application source code
COPY . .

# Start the FastAPI app using Uvicorn
CMD ["python3.10", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
