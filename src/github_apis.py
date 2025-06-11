import os

import requests


GITHUB_PAT = os.environ.get("GITHUB_PAT")

requests_session = requests.Session()
requests_session.headers.update({
    "Authorization": f"Bearer {GITHUB_PAT}",
})


def get_repo_language_distribution(repo_languages_url):
    response = requests_session.get(repo_languages_url)
    
    response_data = response.json()

    total_num_bytes = 0
    for language_name, num_bytes in response_data.items():
        total_num_bytes += num_bytes
    
    languages_distrib_strs = []
    for language_name, num_bytes in response_data.items():
        percentage = 100 * num_bytes / total_num_bytes
        distrib_str = f"{language_name}: {round(percentage, 2)} %"
        languages_distrib_strs.append(distrib_str)

    combined_distrib_str = "; ".join(languages_distrib_strs)
    return combined_distrib_str


def get_repo_metadata(repo_endpoint):
    url = "https://api.github.com/repos/" + repo_endpoint
    
    response = requests_session.get(url)
    
    response_data = response.json()
    
    return response_data

def get_contributions(contributors_url, steps=[5, 10, 15, 20, 25, 30, 35, 40, 50, 75, 100]):
    response = requests_session.get(contributors_url + "?per_page=100")
    response_data = response.json()

    commitsAt = {}
    for step in steps:
        if step > len(response_data):
            break

        commitsAt[f"commits@{step}"] = response_data[step - 1]['contributions']

    return commitsAt


def get_repo_info(repo_endpoint):
    metrics = {}

    repo_metadata = get_repo_metadata(repo_endpoint)
    
    metrics['stars'] = repo_metadata.get('stargazers_count', "N/A")
    metrics['open_issues'] = repo_metadata.get('open_issues_count', "N/A")

    languages_url = repo_metadata.get('languages_url', None)
    language_distribution = "N/A"
    if languages_url is not None:
        language_distribution = get_repo_language_distribution(languages_url)
    metrics['language_distribution'] = language_distribution

    contributors_url = repo_metadata.get('contributors_url', None)
    if contributors_url is not None:
        commitsAt = get_contributions(contributors_url)
        metrics = {
            **metrics,
            **commitsAt
        }
    
    return metrics
