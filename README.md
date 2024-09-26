# ML Model as an API using GitHub Actions for CI/CD

![image](https://github.com/user-attachments/assets/ef3a1848-8ff7-4e37-bb0b-7ec24d262e28)

## Overview

Welcome to the Sentiment Analysis API! This cutting-edge project showcases the power of Continuous Integration and Continuous Deployment (CI/CD) using GitHub Actions to automate the workflow for testing, building, and deploying a state-of-the-art sentiment analysis model.

At its core, this API utilizes a Transformer model specifically designed to accurately predict the sentiment of any given statement. Built on the DistilBERT architecture—an efficient and lightweight variant of BERT—this model has been fine-tuned for sentiment classification, ensuring top-notch performance.

## Key Features

- **State-of-the-Art Sentiment Analysis**: Leverage a powerful **DistilBERT** Transformer model for accurate sentiment classification of text, enabling you to understand the emotional tone of user statements.

- **FastAPI Framework**: Built using **FastAPI**, this API offers high performance and easy integration, providing a smooth experience for developers when accessing sentiment predictions.

- **Automated CI/CD**: Utilize **GitHub Actions** to implement Continuous Integration and Continuous Deployment, automating testing, building, and deployment processes for seamless updates.

- **Dockerized Application**: The entire application is **dockerized**, ensuring consistent behavior across different environments and simplifying the deployment process.

- **Easy Deployment on Render**: The API is deployed on **Render**, allowing for quick and hassle-free access to the sentiment analysis service without the need for complex server setups.

- **User-Friendly API**: Enjoy a well-documented and easy-to-use RESTful API that makes integrating sentiment analysis capabilities into your applications straightforward.

- **Scalable Solution**: Designed to handle varying loads, the API can scale to meet the demands of different applications, making it suitable for both small projects and larger enterprise solutions.


## Explore the API
To explore the API and try out predictions, visit the following deployed URL:
https://sa-cicd.onrender.com/predict

## Using curl in the terminal:
```
curl -X POST "https://sa-cicd.onrender.com/predict" \
-H "Content-Type: application/json" \
-d '{"text": "I love this product!"}'

```

## Using Python (with requests library):
```
import requests

url = "https://sa-cicd.onrender.com/predict"
data = {"text": "I love this product!"}
response = requests.post(url, json=data)

print(response.json())

```
Both methods will send the text as JSON to the API and return the sentiment prediction.

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
   git clone https://github.com/bhardwaj-di/SA_CICD.git
    
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
