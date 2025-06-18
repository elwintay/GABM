# GABM Project

## Description

This repository contains the setup for the `gemini-fastapi` service, which is deployed using Docker Compose. The service leverages NVIDIA GPUs for accelerated computing and runs a FastAPI application.

## Prerequisites

Before you begin, ensure you have the following installed:

- Docker (version 19.03 or later)
- NVIDIA Container Toolkit
- Docker Compose (version 3.8 or later)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/GABM.git
   ```

2. Navigate to the project directory:
   ```bash
   cd GABM
   ```

3. Create a `.env` file in the root directory to define environment variables. Example:
   ```env
   GEMINI_API_KEY=[YOUR_API_KEY]
   ```

## Usage

### Running the Service

To start the `gemini-fastapi` service, use the following command:

```bash
docker-compose up -d
docker exec -it "YOUR DOCKER CONTAINER TAG" /bin/bash
```

This will:

- Map port `8000` on the host to port `8000` in the container.
- Mount the current directory (`.`) to `/gabm` inside the container.
- Enable GPU acceleration using NVIDIA runtime.

### Accessing the Application

Once the service is running, you can access the FastAPI application at:

```
http://localhost:8000
```

### Stopping the Service

To stop the service, use:

```bash
docker-compose down
```

## Configuration

### Environment Variables

The `.env` file is used to configure runtime settings. Ensure the following variables are defined:

- `NVIDIA_VISIBLE_DEVICES`: Specifies which GPUs are visible to the container.
- `NVIDIA_DRIVER_CAPABILITIES`: Defines the GPU capabilities required by the container.

### Custom Commands

To startup the FastAPI server startup command

```yaml
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Contributing

If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or feedback, please reach out:

- Email: your-email@example.com
- GitHub: [your-username](https://github.com/your-username)