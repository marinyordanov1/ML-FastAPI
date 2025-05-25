# Demo ML API with FastAPI

This repository hosts a simple machine learning inference service built with FastAPI. It loads a pre-trained scikit-learn model from `model/model.pkl` and exposes a REST endpoint for generating predictions based on numeric feature inputs.

## Features

- **FastAPI** server for high-performance asynchronous inference
- **Predict** endpoint accepting JSON inputs and returning JSON outputs
- **Docker** support for easy containerized deployment

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Running Locally](#running-locally)
  - [API Endpoint](#api-endpoint)
  - [Docker](#docker)
- [Project Structure](#project-structure)
- [Model Details](#model-details)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/demo-ml-api.git
   cd demo-ml-api
   ```
2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install --no-cache-dir -r requirements.txt
   ```

## Usage

### Running Locally

Start the FastAPI server with Uvicorn:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Server will be available at `http://localhost:8000`.

### API Endpoint

**POST** `/predict`

- **Request Body**:
  ```json
  {
    "features": [float, float, ...]
  }
  ```
- **Response**:
  ```json
  {
    "prediction": float
  }
  ```

Example with `curl`:
```bash
curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

### Docker

Build the Docker image:
```bash
docker build -t demo-ml-api .
```

Run a container:
```bash
docker run -d -p 8000:8000 demo-ml-api
```

## Project Structure

```
Demo/
├── Dockerfile            # Docker configuration
├── requirements.txt      # Python dependencies
├── app/
│   ├── main.py           # FastAPI application
│   └── model.py          # MLModel wrapper
└── model/
    └── model.pkl         # Pre-trained scikit-learn model
```

## Model Details

The `MLModel` class in `app/model.py` loads the pickled model and provides a `predict` method. Input features are validated to ensure they are numeric and then passed to the scikit-learn model. Errors during prediction return HTTP 400 or 500 codes accordingly.
