# FastAPI Sentiment Analysis API


![alt text](image.png)

## Overview

This project implements a **Sentiment Analysis API** using a **Transformer model** to predict the sentiment of a given statement. The model is based on the **DistilBERT** architecture, a lightweight version of BERT, fine-tuned for sentiment classification. The API is built with **FastAPI** and serves predictions as a web service, allowing easy integration into various applications. The entire application is **dockerized** and deployed on **Render**, providing a seamless experience for developers.

## Explore the API
To explore the API and try out predictions, visit the following deployed URL:
https://sa-cicd.onrender.com/predict

## Features

- **Predict Sentiments**: Classifies input text as "positive" or "negative".
- **FastAPI**: Built using FastAPI, ensuring high performance and easy-to-use endpoints.
- **Dockerized**: Fully containerized application for easy deployment and scalability.
- **Hosted on Render**: Deployed to the cloud, making it accessible from anywhere.

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [Transformers](https://huggingface.co/transformers/)
- [PyTorch](https://pytorch.org/)
- [Docker](https://www.docker.com/)
- [Render](https://render.com/)

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Docker (optional, for local development)

### Installation

1. **Clone the repository**:
   ```bash
    https://github.com/bhardwaj-di/SA_CICD.git
    
2. Install dependencies: You can install the dependencies using pip
    ```
    pip install -r requirements.txt

### Running Locally
To run the API locally, use the following command:
   ```
    uvicorn app:app --host 0.0.0.0 --port 8000

```

### Using Docker
1. Build the Docker image:
    ```
    docker build -t fastapi-sentiment-api .
2. Run the Docker container:
    ```
    docker run -d -p 8000:10000 fastapi-sentiment-api

### API Usage
Once the API is running, you can make requests to the following endpoint:
POST /predict

Request Body:
   ```
{
  "text": "I love this product!"
}
```

Response:
 ```
    {
  "prediction": "positive"
}
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or want to add new features, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
