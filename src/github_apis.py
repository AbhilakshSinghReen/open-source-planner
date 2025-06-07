import requests


requests_session = requests.Session()


def get_repo_metadata(repo_endpoint):
    url = "https://api.github.com/repos/" + repo_endpoint
    
    response = requests_session.get(url)
    
    response_data = response.json()
    
    return response_data
