# Sentiment Analysis

## Project Description 

A binary classification model to identify CSEM-related text from the non-CSEM text.

## Using the docker image

1. Log in your GitLab account using the command: 
```
docker login grace-gitlab.grace-fct.eu
```
2. Create and run a container instance of the docker image in Gitlab. The service will work on port **9066** 
```
docker run --name CONTAINER_NAME  -p 9066:9066  grace-gitlab.grace-fct.eu/grace/wp4-ule-sentiment-analysis
```

Once the container is running, you can send POST request to query the tool.

## Usage
You can send a request as form-data  via Postman of Python:

```python
import requests

url = 'http://localhost:9066/classify_sentiment'
d_json = {'text': "Some text to be classified"}

r = requests.post(url, json=d_json)
print(r.text)
```

### Output
```json
{"cat":"No-CSEM","conf":0.97}
```

## Maintainers

* [@Wesam Alnabki](mailto:wesam.alnabki@ule.es)

## Known Issues

- The model is binary classification trained on a small CSEM-related dataset.
