# FROM pytorch/pytorch:2.2.2-cuda11.8-cudnn8-runtime
FROM pytorch/pytorch:2.7.0-cuda12.8-cudnn9-runtime

# Install optional system packages
RUN apt-get update && apt-get install -y git

# Set the working directory
WORKDIR /workspace

# Copy requirements.txt into the image
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the port FastAPI will run on
EXPOSE 8000

# Optional sanity check
RUN python -c "import torch; print('PyTorch version:', torch.__version__)"
